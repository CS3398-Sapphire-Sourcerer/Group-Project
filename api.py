# this file will handle the api calls between the server and client
from init import socketio, SocketIO , app, datab
import flask


@socketio.on('connect')
def on_connect():
    # get the connecting user's user ID
    # flask.session works in socket IO handlers :)
    uid = flask.session.get('auth_user', None)
    if uid is None:
        app.logger.warn('received socket connection from unauthed user')
        return

    app.logger.info('new client connected for user %d', uid)

    # add this connection to the user's 'room', so we can send to all
    # the user's open browser tabs
    socketio.join_room('user-{}'.format(uid))


@socketio.on('disconnect')
def on_disconnect():
    app.logger.info('client disconnected')