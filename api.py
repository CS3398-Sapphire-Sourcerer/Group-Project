# this file will handle the api calls between the server and client
from init import socketio, SocketIO, app, datab
import flask_socketio
import flask
import models
import questionLogic

user_question_session = None;

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
    user.Building = 1
    user_building = 1
    # send lat and long to the building function to determine which building the user is in
    # return the building and save it in the user class
    datab.session.commit()
    flask_socketio.emit('enterBuilding', {"building": user_building}, room='user-{}'.format(uid))


@socketio.on('generateQuestions')
def question_serv(cli):
    uid = cli['userID']
    bldid = cli['buildingID']

    print ("****Question was called****")

    print("Building ID:")
    print (bldid)

    user_question_session= questionLogic.question_handler(uid, bldid) #Create question session, or pull session if it exist
    Q_obj = user_question_session.serializeCurrentQuestion()

    #print (Q_handler.serializeCurrentQuestion())

    socketio.emit('question', Q_obj, room='user-{}'.format(uid))

@socketio.on('answer')
def answer_question(cli):
    print("****answer****")
    app.logger.info("****Answer****")
    # call the database and test the answer and question
    userAnswer = cli['userAnswerId']
    questionID = cli['questionId']

    questionObj = models.Question.query.get(questionID)

    if userAnswer is questionObj.q_answer:
        print("You got it right!")
        result = "You got it right!"
    else:
        print("You got it wrong :(")
        result = "You got it wrong."

    # delete database question entry from stack
    # TODO: flask.session.get(uid)? add delete to session object

    socketio.emit('result', result) #result = some boolean based on if above

    # if no more questions, emit end status

    # TODO: get user at max test from questionLogic
    #socketio.emit('qLimit') #qLimit = some message saying "Reached max for today, try again tomorrow"

    # TODO : recalculate state on the basis of a correct question.
    # updateState()

    user_question_session.nextQuestionIndex()
    Q_obj = user_question_session.serializeCurrentQuestion()

    uid = flask.session.get('auth_user')

    socketio.emit('question', Q_obj, room='user-{}'.format(uid))


