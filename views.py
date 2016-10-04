#views.py is the file that will be handling the creating of the html pages and the routing of the browser URLS

#these import libraries
from flask import Flask
import flask


#generates the app
app = Flask(__name__)


#this is the function that will show the user the home.html page
#@app.route('/', methods = ['GET'])
#def splash_screen():
#
#    names = 'bobby hill'
#    return flask.render_template('home.html', person=names)


#this function displays the html page that contains the forms for the signup page
#It is a GET page because it is sending data to the user, and not receiving the form data...yet
@app.route('/signup', methods=['GET'])
def signup_forms():
    return flask.render_template('signup.html', state = 'first_attempt_at_signup_for_user_session')

#This function pairs with the previous because when the user clicks submit, It is sending data back to the server using
# a "POST" request. This will allow this python function to scrape the form data from the request, assign to variables,
# and store int the database and or reject the user if they do not enter a valid email address to sign up.
@app.route('/signup', methods=['POST'])
def signup_submission():
    #this next few commands will be stripping out the form data from the html file signup.html when the user submits
    userName = flask.request.form['user'] # 'user' refers to the label 'user' for the form input in the html file
    password1 = flask.request.form['passord1'] # 'password1 refers to the form input with the label password1
    password2 = flask.request.form['passord2']  # This makes sure the two password form inputs are the same



if __name__ == '__main__':
    app.run()

