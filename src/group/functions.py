from flask_pymongo import PyMongo
from flask import jsonify
from .models import Group
from datetime import datetime
from .models import Group
from db import mongo 

def create_group(data):
    group_name = data.get('group_name')
    print(group_name)
    if not mongo.db.groups.find_one({"group_name": group_name}):
        group = Group(group_name=group_name)
        mongo.db.groups.insert_one(group.to_dict())
        return jsonify({'message': 'Group created successfully.'}), 200
    else:
        return jsonify({'error': 'Group name already taken.'}), 400

def add_user_to_group(data):
    group_name = data.get('group_name')
    username = data.get('username')
    group = mongo.db.groups.find_one({"group_name": group_name})
    if not group:
        return jsonify({'error': 'Group not found.'}), 404
    if username in group['members']:
        return jsonify({'info': 'User already in group.'}), 400
    group['members'][username] = datetime.utcnow()
    mongo.db.groups.update_one({"group_name": group_name}, {"$set": group})
    return jsonify({'message': 'User added to group successfully.'}), 200

def get_group_messages(data):
    group_name = data.get('group_name')
    username = data.get('username')
    messages = mongo.db.messages.find({
        "$or": [
            {"group_id": group_name, f"is_read.{username}": {"$exists": True}},
            {"group_id": group_name, "sender_id": username}  # Added condition for sender
        ]
    })
    
    # Convert ObjectId to string for JSON serialization
    return jsonify({'messages': [{**message, '_id': str(message['_id'])} for message in messages]})