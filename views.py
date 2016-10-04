# views.py is the file that will be handling the creating of the html pages and the routing of the browser URLS

# these import libraries
from flask import Flask
import flask


# generates the app
app = Flask(__name__)


# this is the function that will show the user the home.html page
# @app.route('/', methods = ['GET'])
# def splash_screen():
#
#    names = 'bobby hill'
#    return flask.render_template('home.html', person=names)

# TODO create a signup.html file within templates
# this function displays the html page that contains the forms for the signup page
# It is a GET page because it is sending data to the user, and not receiving the form data...yet
@app.route('/signup', methods=['GET'])
def signup_forms():
    return flask.render_template('signup.html', state = 'first_attempt_at_signup_for_user_session')

# This function pairs with the previous because when the user clicks submit, It is sending data back to the server using
# a "POST" request. This will allow this python function to scrape the form data from the request, assign to variables,
# and store int the database and or reject the user if they do not enter a valid email address to sign up.
# *******************the email validation will come after the integration of the front and backend for this page
@app.route('/signup', methods=['POST'])
def signup_submission():
    # this next few commands will be stripping out the form data from the html file signup.html when the user submits
    user_name = flask.request.form['user']  # 'user' refers to the label 'user' for the form input in the html file
    password1 = flask.request.form['password1']  # 'password1 refers to the form input with the label password1
    password2 = flask.request.form['password2']  # This makes sure the two password form inputs are the same

    # These next few lines are for checking passwords and making sure user name is long enough, if any of the conditions
    # fail they will route the user back to the signup page with the forms cleared with a failure message, The state
    # variable that is included in the flask.render is to inform the user why the signup failed
    if password1 != password2:
        return flask.render_template('signup.html', state='Passwords did not match')
    if (len(user_name)) > 20:
        return flask.render_template('signup.html', state='User name is too long')
    if (len(user_name)) < 8:
        return flask.render_template('signup.html', state='User name is too short')
    # Test the database to determine if username is already taken to prevent duplicates
    # existing = **DATABASE QUERY** models.User.query.filter_by(login=user_name).first()
    # if existing is not None:
    #    return flask.render_template('signup.html', state='User name is already taken')
    # <input type="hidden" name="url" value="{{ request.args.url }}"> goes into the html for token/session auth
    #
    # @@@ Starting here we know the user submission passed and we will input the variables into the database
    # user = models.User() # This line creates the database object for users
    # user.login = user_name # This stores the user_name into the login field in the user database object
    # user.pass_hash =  bcrypt.hashpw(password1.encode('utf8'), bcrypt.gensalt(15)) # this encrypts and stores the hash
    # db.session.add(user) # this adds the object to the database submit queue
    # db.session.commit() # this is the actual storing of the database object into database, similar to git operations
    # flask.session['auth_user'] = user.id # this stores the session key information for the user into the database,
    # # session keys keep track of users currently logged into the app, this is information that the browser generates
    # # but flask is able to extract to create a "Temp user ID" so we can know whos logged in and to authenticate their
    # # actions while logged into this "Session"





if __name__ == '__main__':
    app.run()

