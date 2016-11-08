from flask import Flask
import flask_sqlalchemy
from flask_socketio import SocketIO
import eventlet
eventlet.monkey_patch()


# generates the app
app = Flask(__name__)
# load the admin password as well as set up the database
app.config.from_pyfile('settings.py')
datab = flask_sqlalchemy.SQLAlchemy(app)

async_mode = "eventlet"
socketio = SocketIO(app, async_mode=async_mode)
