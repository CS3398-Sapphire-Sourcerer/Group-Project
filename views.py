# views.py is the file that will be handling the creating of the html pages and the routing of the browser URLS

# these import libraries
import base64
import os
import flask
import models
from init import app, datab





@app.before_request
def setup_user():
    # authentication token so that we know when a user is logged in while broswing
    if 'auth_user' in flask.session:
        user = models.User.query.get(flask.session['auth_user'])
        flask.g.user = user


# this is the function that will show the user the home.html page
@app.route('/', methods=['GET'])
def splash_screen():
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
    user.pass_word = password1
    user.email = email
    # user.pass_hash =  bcrypt.hashpw(password1.encode('utf8'), bcrypt.gensalt(15)) # this encrypts and stores the hash
    datab.session.add(user)  # this adds the object to the database submit queue
    datab.session.commit()  # this is the actual storing of the database object into database, similar to git operations
    flask.session['auth_user'] = user.id  # this stores the session key information for the user into the database,
    # # session keys keep track of users currently logged into the app, this is information that the browser generates
    # # but flask is able to extract to create a "Temp user ID" so we can know whos logged in and to authenticate their
    # # actions while logged into this "Session"
    return flask.redirect(flask.url_for('splash_screen'))


@app.route('/users/', methods=['GET'])
def users_default():
    u = models.User.query.all()         #get all users
    users = list(u)                     #save all users in a list format, pass list to users.html
    return flask.render_template('users.html', users=users)

@app.route('/users/<int:uid>', methods=['GET'])
def users_profile(uid):
    tempUser = models.User.query.get(uid)

    if tempUser is None:
        #user does not exist at that id, go to 404 page.
        flask.abort(404)
    else:
        return flask.render_template('user_profile.html', userInfo=tempUser, uid=uid)


# TODO app.route('/app')

@app.route('/teams', methods=['GET'])
def team_page():
    return flask.render_template('teams.html')

@app.route('/signin', methods=['GET'])
def sign_in():
    # this is the page displaying the sign in forms, which is accessed from the nav bar. This will connect to the POST
    # method of the signin.html page.
    return flask.render_template('signin.html', state='good')


@app.route('/signin', methods=['POST'])
def sign_in_submit():
    user_name = flask.request.form['username']  # this pulls the form data for the user login
    pass_word = flask.request.form['password']  # this pulls the form data for the user pass word

    user = models.User.query.filter_by(user_name=user_name).first()
    # @@@@ here is where we will call the data base to ensure the user exists and if they have valid pass word and
    if user is not None:
        if pass_word == user.pass_word:
            flask.session['auth_user'] = user.id
            return flask.redirect(flask.url_for('splash_screen'))

    return flask.render_template('signin.html', state='bad')

@app.route('/logout')
def handle_logout():
    del flask.session['auth_user']
    return flask.redirect(flask.request.args.get('url', '/'), 303)

@app.errorhandler(404)
def bad_page(err):
    return flask.render_template('404.html'), 404

