# this file will handle the api calls between the server and client
from init import socketio, SocketIO, app, datab
import flask_socketio
import flask
import models
import questionLogic
from state import requestState, updateState

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
    flask_socketio.join_room('user-{}'.format(uid))


@socketio.on('disconnect')
def on_disconnect():
    uid = flask.session.get('auth_user', None)
    if uid is None:
        app.logger.warn('received socket connection from unauthed user ', uid)
        return

    flask_socketio.close_room('user-{}'.format(uid))
    app.logger.info('client disconnected')


@socketio.on('ready')
def readyState(obj):
    uid = flask.session.get('auth_user', None)
    if (not obj):
        print ("Setting response:")
        response = requestState({"type": "new"}) #TODO, Fix Error, response is being set to NULL!
        print("Response is:")
        print (response)
        flask_socketio.emit('stateFullUpdate', response, room='user-{}'.format(uid))

#TODO FIX CHECK LOCATION using building short codes
def check_location(user_location):
    latitude = user_location['latitude']
    longitude = user_location['longitude']



@socketio.on('changeLocation')
def location_change(u_loc):
    #TODO: u_loc has building short code and "continuous" int, 0 send question, 1 do nto send question

    if u_loc != None:
        app.logger.info('received user location')

    else:
        app.logger.info('did not receive user location')
        return

    # TODO, pull out building
    # TODO, if building is not empty, pull out via shortcode
    b_shortcode = u_loc['building']
    print ("In location change, building code is:")
    print (b_shortcode)
    b = models.Building.query.filter_by(building_shortcode = b_shortcode)

    uid = u_loc['uid']
    latitude = u_loc['latitude']
    longitude = u_loc['longitude']

    print(latitude, " ", longitude)
    user = models.User.query.get(uid)
    print(user.email)

    # TODO KILL ME V
    user_building = b.id
    user.Building = b.id
    
    # send lat and long to the building function to determine which building the user is in
    # return the building and save it in the user class
    datab.session.commit()

    #TODO, if structure to verify building data from client, check against expected building code
        #TODO, if not in building, update location and aquknowldege
        #TODO, if in building, then question_serv()

    flask_socketio.emit('enterBuilding', {"building": user_building}, room='user-{}'.format(uid))

#This method works with the change location function to determine if a long/lat coordinate is actually inside the expect
#building. Buildings are given by the building shortcode.
def pointWithinBuilding(longitude, latitude, b_code):
    building = models.Building.query.filter_by(building_shortcode = b_code).first()
    coordinate_list = models.coordinate_point.query.filter_by(building.id)
    coordinate_list = list(coordinate_list)




#@socketio.on('generateQuestions')
def question_serv(uid, bldid):
    # TODO make sure we are using building short codes
    #uid = cli['userID']

    #TODO, bldID is coming back null. Check sender.
    #bldid = cli['buildingID']

    print ("****Question was called****")

    print("Building ID:")
    print(bldid)

    user_question_session= questionLogic.question_handler(uid, bldid) #Create question session, or pull session if it exist
    if user_question_session.session_is_closed:
        socketio.emit('noMoreQuestions', {'result': "You are out of questions"}, room='user-{}'.format(uid))
    else:
        Q_obj = user_question_session.serializeCurrentQuestion()
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

    uid = flask.session.get('auth_user')
    user = models.User.query.get(uid)
    user_question_session = questionLogic.question_handler(user.id, user.building)
    user_question_session.removeAnsweredQuestion()
    Q_obj = user_question_session.serializeCurrentQuestion()

    print("Sending next question")
    print(Q_obj)


    socketio.emit('question', Q_obj, room='user-{}'.format(uid))


