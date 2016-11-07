from flask import Flask
import flask_sqlalchemy
from flask_socketio import SocketIO

# generates the app
app = Flask(__name__)
# load the admin password as well as set up the database
app.config.from_pyfile('settings.py')
datab = flask_sqlalchemy.SQLAlchemy(app)


socketio = SocketIO(app)
