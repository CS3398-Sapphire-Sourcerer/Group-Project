# this file will handle the api calls between the server and client
from init import socketio, SocketIO, app, datab
import flask_socketio
import flask
import models



@socketio.on('connect')
def on_connect():
    # get the connecting user's user ID
    # flask.session works in socket IO handlers :)
    uid = flask.session.get('auth_user', None)
    if uid is None:
        app.logger.warn('received socket connection from unauthed user ', uid)
        return

    app.logger.info('new client connected for user %d', uid)

    # add this connection to the user's 'room', so we can send to all
    # the user's open browser tabs
    #socketio.join_room('user-{}'.format(uid))
    flask_socketio.join_room('user-{}'.format(uid))

@socketio.on('disconnect')
def on_disconnect():
    uid = flask.session.get('auth_user', None)
    if uid is None:
        app.logger.warn('received socket connection from unauthed user ', uid)
        return

    flask_socketio.close_room('user-{}'.format(uid))
    app.logger.info('client disconnected')

@socketio.on('changeLocation')
def location_change(u_loc):
    if u_loc != None:
        app.logger.info('received user location')

    else:
        app.logger.info('did not receive user location')
        return

    uid = u_loc['uid']
    lat = u_loc['latitude']
    long = u_loc['longitude']

    print(lat, " ", long)
    user = models.User.query.get(uid)
    print(user.email)
    user.building = 3
    user_building = 3
    # send lat and long to the building function to determine which building the user is in
    # return the building and save it in the user class
    datab.session.commit()
    flask_socketio.emit('enterBuilding', {"building": user_building}, room='user-{}'.format(uid))


