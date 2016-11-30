# views.py is the file that will be handling the creating of the html pages and the routing of the browser URLS

# these import libraries
import base64
import os
import bcrypt
import flask
import models
import questionLogic
import majorIDs
from init import app, datab
from flask import request
from state import initializeGame, game
from sqlalchemy import desc
import json


@app.before_first_request
def gameSetup():
    populate_buildings()
    initializeGame()


@app.before_request
def setup_user():
    if 'auth_user' in flask.session:
        user = models.User.query.get(flask.session['auth_user'])
        test = flask.session['auth_user']
        print("AUTH_USER:", test)
        if user is None:
            # old bad cookie, no good
            del flask.session['auth_user']
        # save the user in `flask.g`, which is a set of globals for this request
        flask.g.user = user
    #initializeGame()



# this is the function that will show the user the home.html page
@app.route('/', methods=['GET'])
def splash_screen():
    if flask.session.get('auth_user') is not None:
        return flask.redirect("/app", 302)
    return flask.render_template('index.html')


# this function displays the html page that contains the forms for the signup page
# It is a GET page because it is sending data to the user, and not receiving the form data...yet
@app.route('/signup', methods=['GET'])
def signup_forms():
    return flask.render_template('signup.html')


# This function pairs with the previous because when the user clicks submit, It is sending data back to the server using
# a "POST" request. This will allow this python function to scrape the form data from the request, assign to variables,
# and store int the database and or reject the user if they do not enter a valid email address to sign up.
# *******************the email validation will come after the integration of the front and backend for this page
@app.route('/signup', methods=['POST'])
def signup_submission():
    # this next few commands will be stripping out the form data from the html file signup.html when the user submits
    user_name = flask.request.form['username']  # 'user' refers to the label 'user' for the form input in the html file
    password1 = flask.request.form['password1']  # 'password1 refers to the form input with the label password1
    password2 = flask.request.form['password2']  # This makes sure the two password form inputs are the same
    email = flask.request.form['email']
    # These next few lines are for checking passwords and making sure user name is long enough, if any of the conditions
    # fail they will route the user back to the signup page with the forms cleared with a failure message, The state
    # variable that is included in the flask.render is to inform the user why the signup failed
    if password1 != password2:
        return flask.render_template('signup.html', state='Passwords did not match')
    if (len(user_name)) > 20:
        return flask.render_template('signup.html', state='User name is too long')
    if (len(user_name)) < 1:
        return flask.render_template('signup.html', state='User name is too short')
    # Test the database to determine if username is already taken to prevent duplicates
    existing = models.User.query.filter_by(user_name=user_name).first()
    if existing is not None:
        return flask.render_template('signup.html', state='User name is already taken')
    # <input type="hidden" name="url" value="{{ request.args.url }}"> goes into the html for token/session auth

    # @@@ Starting here we know the user submission passed and we will input the variables into the database
    user = models.User()  # This line creates the database object for users
    user.user_name = user_name  # This stores the user_name into the login field in the user database object
    #user.pass_word = password1
    user.pass_word = bcrypt.hashpw(password1.encode('utf8'), bcrypt.gensalt(15))
    user.email = email
    # user.pass_hash =  bcrypt.hashpw(password1.encode('utf8'), bcrypt.gensalt(15)) # this encrypts and stores the hash
    datab.session.add(user)  # this adds the object to the database submit queue
    datab.session.commit()  # this is the actual storing of the database object into database, similar to git operations
    flask.session['auth_user'] = user.id  # this stores the session key information for the user into the database,
    # # session keys keep track of users currently logged into the app, this is information that the browser generates
    # # but flask is able to extract to create a "Temp user ID" so we can know whos logged in and to authenticate their
    # # actions while logged into this "Session"
    return flask.redirect(flask.url_for('splash_screen'))


# Populate question forms
@app.route('/see_questions', methods=['GET'])
def question_session_display():
    building = models.Building.query.filter_by(name="Derek").first()

    if flask.g.user and building:
        question_session = None
        question_session = questionLogic.question_handler(flask.g.user.id, building.id)
        # print(question_session.serializeCurrentQuestion() )
        return flask.render_template('temp_question_display.html', question_session=question_session)
    else:
        print("Error in building session, printing with None")
        return flask.render_template('temp_question_display.html', question_session=None)


@app.route('/questions', methods=['GET'])
def question_forms():
    return flask.render_template('question_submission.html')


# Adding route for question and answer submission
@app.route('/questions', methods=['POST'])
def question_submission():
    # Get info
    question_text = flask.request.form['Question']
    question_type = int(flask.request.form['Type'])
    answer_text = flask.request.form['Answer']

    q = questionLogic.q_database_manager

    q.addQuestionWithAnswer(question_text, question_type, answer_text)

    # TODO, return successful state if good data, poor state if not
    return flask.redirect(flask.url_for('question_submission'))


# Added test route for quick question adding for test
@app.route("/generate_questions", methods=['GET'])
def question_creation():
    query = models.Question.query.first()
    if query is None:
        q = questionLogic.q_database_manager()
        q.addQuestionWithAnswer("Which language requires a virtual machine enviorment to run?", "1", "Java")
        q.addQuestionWithAnswer("Which language allows for manipulation of pointers?", "1", "C++")
        q.addQuestionWithAnswer("Which language controlls scope by using indentation levels?", "1", "Python")
        q.addQuestionWithAnswer("Which language is a hypertext mark-up language?", "1", "HTML")
        q.addQuestionWithAnswer("Which language is a vitual hardware language?", "1", "VHDL")

        q.addBuilding("Derek", "1")
    return flask.redirect(flask.url_for('question_submission'))

#add route to populate the DB
#TODO add the building types into buildings.json then add sunctionallity into populate_buildings()
#TODO function so that it stores the building type
def populate_buildings():
    query = models.Building.query.first()
    if query is None:
        obj = None #create an object to store json data
        new_building = models.Building() #create object for individual building
        new_coordinate = models.coordinate_point() #create object for coordinates

        #open json file as read only
        with open('static\\buildings.json', 'r') as building_list:
            obj = json.load(building_list)
        for build_count in obj["buildings"]:
            new_building.name = build_count["buildingName"]
            print("name: ", new_building.name)
            datab.session.add(new_building)
            datab.session.commit() #commit the building so we have an ID associated to store with coordinates

            for coord_count in build_count["coordinates"]:
                print("In coord loop")
                new_coordinate.long = coord_count["lng"]
                print("lng: ", new_coordinate.long)
                new_coordinate.lat = coord_count["lat"]
                print("lat: ", new_coordinate.lat)
                new_coordinate.building_group = new_building.id
                datab.session.add(new_coordinate)

            datab.session.commit()#commit all the coordinates at once



@app.route('/users/', methods=['GET'])
def users_default():
    u = models.User.query.all()  # get all users
    users = list(u)  # save all users in a list format, pass list to users.html
    return flask.render_template('users.html', users=users)


@app.route('/users/<int:uid>', methods=['GET'])
def users_profile(uid):
    tempUser = models.User.query.get(uid)

    if tempUser is None:
        # user does not exist at that id, go to 404 page.
        flask.abort(404)

    return flask.render_template('user_profile.html', userInfo=tempUser, uid=uid)


# this function display the user edit fields
# TODO: query what is already present in the fields if they exist
@app.route('/users/<int:uid>/updateInfo', methods=['GET'])
def user_edit(uid):
    tempUser = models.User.query.get(uid)
    if tempUser is None:
        # user does not exist at that id, go to 404 page.
        flask.abort(404)

    return flask.render_template('edit_user_profile.html', userInfo=tempUser, uid=uid)


@app.route('/users/<int:uid>/updateInfo', methods=['POST'])
def update_user_profile(uid):
    # query user
    user = models.User.query.get(uid)
    # scrape form data
    bio = flask.request.form['bio']
    major = flask.request.form['major']

    user.user_profile_text = bio
    user.major = major
    datab.session.add(user)
    datab.session.commit()
    return flask.redirect(flask.url_for('users_profile',uid=uid))


@app.route('/teams', methods=['GET'])
def team():
    return flask.render_template('teams.html')


@app.route('/team/<int:team_id>', methods=['GET'])
def team_page(team_id):
    users = models.User.query.filter_by(team=team_id)
    users = list(users)
    team = models.Team.query.get(team_id)

    return flask.render_template('team_page.html', rooster=users, teamInfo=team)


@app.route('/signin', methods=['GET'])
def sign_in():
    # this is the page displaying the sign in forms, which is accessed from the nav bar. This will connect to the POST
    # method of the signin.html page.
    return flask.render_template('signin.html', state='good')

@app.route('/leaderBoard', methods = ['GET'])
def leader_board():
    #this is the page for displaying the leaderboard for the top 10 players for everyteam. It will have access
    #through the navi bar and filter the players with the highest scores
    leaders = models.User.query.order_by(desc(models.User.Score)).limit(10).all()
    return flask.render_template('leaderBoard.html', winnerCircle = leaders)


@app.route('/signin', methods=['POST'])
def sign_in_submit():
    user_name = flask.request.form['username']  # this pulls the form data for the user login
    pass_word = flask.request.form['password']  # this pulls the form data for the user pass word

    user = models.User.query.filter_by(user_name=user_name).first()
    # @@@@ here is where we will call the data base to ensure the user exists and if they have valid pass word and
    if user is not None:
        pass_word = bcrypt.hashpw(pass_word.encode('utf8'), user.pass_word)
        if pass_word == user.pass_word:
            flask.session['auth_user'] = user.id
            return flask.redirect(flask.url_for('splash_screen'))

    return flask.render_template('signin.html', state='bad')


@app.route('/logout')
def handle_logout():
    del flask.session['auth_user']
    return flask.redirect(flask.request.args.get('url', '/'), 303)


@app.route('/cjsTest1')
def locTest():
    # user = models.User.query.filter_by(user_name=user_name).first()
    # @@@@ here is where we will call the data base to ensure the user exists and if they have valid pass word and
    # if user is not None:
    #    if pass_word == user.pass_word:
    #        flask.session['auth_user'] = user.id
    #        return flask.redirect(flask.url_for('splash_screen'))

    return flask.render_template('httpRequestTest.html', state='good')


@app.route('/updatePos/<uid>/<lat>/<long>', methods=['POST'])
def updatePos(uid, lat, long):
    uid = int(uid)
    lat = float(lat)
    long = float(long)

    return "hello the end of time"


# @app.route('/users/<int:uid>', methods=['GET'])
# def users_profile(uid):
#    tempUser = models.User.query.get(uid)
#
#    if tempUser is None:
#        #user does not exist at that id, go to 404 page.
#        flask.abort(404)
#    else:
#        return flask.render_template('user_profile.html', userInfo=tempUser, uid=uid)

@app.route('/app', methods=['GET'])
def appPage():

    if flask.session.get('auth_user') is None:
        return flask.redirect("/", 302)

    return flask.render_template('app.html')


@app.errorhandler(404)
def bad_page(err):
    return flask.render_template('404.html'), 404
