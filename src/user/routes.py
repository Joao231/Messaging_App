from flask import Blueprint, request, jsonify
from .functions import register_user, get_user_by_username

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    return register_user(data)

# You can add more user-related routes here (login, update, etc.)
