from flask_pymongo import PyMongo
from flask import jsonify
from .models import User
from db import mongo 

def get_user_by_username(username):
    return mongo.db.users.find_one({"username": username})

def register_user(data):
    username = data.get('username')

    if get_user_by_username(username):
        return jsonify({'error': 'Username already taken.'}), 400

    new_user = User(username=username)
    result = mongo.db.users.insert_one(new_user.to_dict())
    
    return jsonify({'message': 'User registered successfully.', 'user_id': str(result.inserted_id)})
