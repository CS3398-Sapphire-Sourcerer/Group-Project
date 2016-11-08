# this file will handle the api calls between the server and client
from init import socketio, SocketIO, app, datab
import flask_socketio
import flask
import models
import questionLogic



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


@socketio.on('generateQuestions')
def question_serv(cli):
    uid = cli['userID']
    bldid = cli['buildingID']

    Q_handler = questionLogic.question_handler(uid, bldid) #Create question session, or pull session if it exist
    Q_obj = flask.jsonify(Q_handler.serializeCurrentQuestion())

    socketio.emit('question', Q_obj, room='user-{}'.format(uid))

@socketio.on('Answer')
def answer_question(cli):

    # call the database and test the answer and question
    userAnswer = cli['userAnswer']
    questionID = cli['questionID']

    questionObj = models.Question.query.get(questionID)

    if userAnswer is questionObj.q_answer:
        print("You got it right!")
    else:
        print("You got it wrong :(")

    # delete database question entry from stack
    # TODO: flask.session.get(uid)? add delete to session object

    socketio.emit('Result') #result = some boolean based on if above

    # if no more questions, emit end status

    # TODO: get user at max test from questionLogic
    socketio.emit('qLimit') #qLimit = some message saying "Reached max for today, try again tomorrow"


