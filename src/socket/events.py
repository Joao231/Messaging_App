from flask import request
from flask_socketio import SocketIO, join_room, leave_room, emit
from datetime import datetime

from ..helpers.validation_helpers import validate_message_content

from db import mongo 

socketio = SocketIO()

@socketio.on('send_direct_message')
def on_send_direct_message(data):
    sender_id = data['sender_id']
    content = data['content']
    room = data.get('room')
    print(f"Received direct message: {data}")
    
    # Assuming validate_message_content is your validation function
    is_valid, error_msg = validate_message_content(content)
    if not is_valid:
        emit('error', {'error': error_msg})
        return
    
    timestamp = datetime.utcnow()

    message = {
        "type": "direct",
        "sender_id": sender_id,
        "content": content,
        "group_id": room,
        "timestamp": timestamp,
    }
    group = mongo.db.groups.find_one({"group_name": room})
    if group:
        message['is_read'] = {username: False for username in group['members'].keys() if username != sender_id}

    mongo.db.messages.insert_one(message)

    emit('receive_direct_message', {
        'sender_id': sender_id,
        'content': content,
        'timestamp': timestamp.isoformat()
    }, room=room)

@socketio.on('mark_direct_message_read')
# Event to mark direct message as read
def on_mark_direct_message_read(data):

    group_id = data['group_id']
    timestamp = data['timestamp']
    message = mongo.db.messages.find_one({"group_id": group_id, "timestamp": timestamp})
    is_read_keys = message['is_read'].keys()
    is_read_values = [True for _ in is_read_keys]
    is_read_update = dict(zip(is_read_keys, is_read_values))

    mongo.db.messages.update_one(
        {"group_id": group_id, "timestamp": timestamp},
        {"$set": {"is_read": is_read_update}}
    )


@socketio.on('join_room')
def on_join(data):
    username = data['username']
    room = data['room']
    print(f"{username} joining room {room}")
    join_room(room)
    emit('notification', {'msg': f"{username} has joined the room."}, room=room)

@socketio.on('leave_room')
def on_leave(data):
    username = data['username']
    room = data['room']
    print(f"{username} leaving room {room}")
    leave_room(room)
    emit('notification', {'msg': f"{username} has left the room."}, room=room)

@socketio.on('disconnect')
# Event to handle disconnection
def on_disconnect():
    print("Client disconnected")
    username = request.args.get('username')  # Assuming user_id is passed as a query parameter
    print(f"User {username} disconnected")
    mongo.db.users.update_one({"username": username}, {"$set": {"isOnline": False}})
    emit('notification', {'msg': 'A user has disconnected.'}, broadcast=True)

@socketio.on('connect')
def on_connect():
    print("Client connected")

    username = request.args.get('username')  # Assuming user_id is passed as a query parameter
    print(f"User {username} connected")
    mongo.db.users.update_one({"username": username}, {"$set": {"isOnline": True}})


