import socketio
import time
import requests

sio = socketio.Client()

SERVER_URL = "http://localhost:8000"
USERNAME = 'jara'
ROOM = "10"

@sio.event
def connect():
    print(f"User {USERNAME} connected to the server")

@sio.event
def disconnect():
    print(f"User {USERNAME} disconnected from the server")

@sio.event
def receive_direct_message(data):
    if data['sender_id'] != USERNAME:
        print("\033[1A")  # Move up one line
        print(f"{data['sender_id']}: {data['content']}")  # Print sender's message
        print(f"{USERNAME}: ", end='', flush=True)  # Prepare for the next message
        # Trigger the on_mark_direct_message_read event
        sio.emit('mark_direct_message_read', {
            'timestamp': data['timestamp'],
            'group_id': ROOM
        })

@sio.event
def error(data):
    print(f"Error: {data}")

def send_direct_message(sender_id, content, room):
    sio.emit('send_direct_message', {
        'sender_id': sender_id,
        'content': content,
        'room': room
    })

def join_room(username, room):
    print(f"User {username} joining room {room}...")
    sio.emit('join_room', {'username': username, 'room': room})


# Continuously prompt for input to send messages
# Continuously prompt for input to send messages
try:
    response = requests.post(f"{SERVER_URL}/user/register", json={'username': USERNAME})
    if response.status_code == 200:
        print(f"User {USERNAME} registered successfully.")
    else:
        print(f"Username {USERNAME} already exists.")
        #raise Exception("An error occurred while processing user registration request.")

    response = requests.post(f"{SERVER_URL}/group/create", json={'group_name': ROOM})
    if response.status_code == 200:
        print(f"Group {ROOM} created successfully.")        
        response = requests.post(f"{SERVER_URL}/group/add_user", json={'group_name': ROOM, 'username': USERNAME})
        if response.status_code == 200:
            print(f"User {USERNAME} added to group {ROOM} successfully.")
        else:
            print(f"Failed to add user {USERNAME} to group {ROOM}.")
    else:
        print(f"Group {ROOM} already exists.")
        response = requests.post(f"{SERVER_URL}/group/add_user", json={'group_name': ROOM, 'username': USERNAME})
        if response.status_code == 200:
            print(f"User {USERNAME} added to group {ROOM} successfully.")
        else:
            print(f"User {USERNAME} is already in group {ROOM}.")

    response = requests.get(f"{SERVER_URL}/group/messages/{ROOM}?username={USERNAME}")
    if response.status_code == 200:
        messages = response.json()['messages']
    else:
        print(f"Failed to fetch messages for group {ROOM}. Status code: {response.status_code}")

    sio.connect(f"{SERVER_URL}?username={USERNAME}")

    join_room(USERNAME, ROOM)

    for message in messages:
        print(f"{message['sender_id']}: {message['content']}")

    while True:
        message = input(f"{USERNAME}: ")  # Prompt with username
        if message.lower() == 'exit':
            break
        send_direct_message(USERNAME, message, ROOM)
        time.sleep(1)
except KeyboardInterrupt:
    print(f"User{USERNAME} disconnected.")

sio.disconnect()
