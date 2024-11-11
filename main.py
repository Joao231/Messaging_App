from flask import Flask
from src.user.routes import user_blueprint
from src.group.routes import group_blueprint
from db import mongo 
from src.socket.events import socketio
import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

mongo.init_app(app)
socketio.init_app(app, cors_allowed_origins="*")

# Register Blueprints
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(group_blueprint, url_prefix='/group')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000, allow_unsafe_werkzeug=True)