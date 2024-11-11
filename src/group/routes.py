from flask import Blueprint, request, jsonify
from .functions import create_group, add_user_to_group, get_group_messages

group_blueprint = Blueprint('group', __name__)

@group_blueprint.route('/create', methods=['POST'])
def create():
    data = request.json
    print(data)
    return create_group(data)

@group_blueprint.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    return add_user_to_group(data)

@group_blueprint.route('/messages/<group_name>', methods=['GET'])
def get_messages(group_name):
    username = request.args.get('username')
    return get_group_messages({'group_name': group_name, 'username': username})

