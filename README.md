# Group-Project
##	About the project

This project is a location-based, territory controlled, trivia game that allows students (currently at Tx. State) to create a profile, select one of three teams, and answer trivia questions based on the major (i.e. Computer Science, English, Nursing, exc.) of the current building they are in. 

##	Team members

Adam Garcia, Brittany Torelli, Casey Sledge, Claudia Ortiz, Collin Weir, Jeremiah Burks, Kaleb Jacobson

##	Neccessary Libraries f

The program is developed in Pycharm using flask. You can download these libraries using the pycharm package manager which is located within your virtual environment in the project interpreter settings, or you can use the pip tool which will allow for package downloads from the command line. In order to run the program, you will need the following libraries: 

  * Flask
  
  * Flask-GoogleMaps
  
  * Flask-script
  
  * Flask-socketIO
  
  * Jinja2
  
  * MarkupSafe
  
  * SQLAlchemy
  
  * eventlet
  
  * Bcrypt
 
You  will also need to aquire an google API key for the maps access, this key can be inputed inside the api file. This key is unique to whoever is using this project.

## Deployment
There are several different methods to get the project running. For running the project in the command line, you must do the command:
  python3 runserver.py socketserver 
 
To run the server in pycharm:
 you need to right click on the runserver.py and click run and then edit the configuration and type in socketserver 
 
Both of these methods will host the project on either the the 127.0.0.1:8000 or if you type ipconfig on your windows or ifconfig on your mac, you can see your IP address and other systems can type that IP address and the port 8000 to connect your server.

If you are going to host on a server and want it to be accessible on the internet, you need to set up a dns service to point at your servers IP and then run the app locall on the server and use a utility like gunicorn to pass socket connections to the local app.
 
 The documentation for Flask-SocketIO is a great resource for knowing how to host your production ready app and how to scale the architecture to manage load balancing and other at scale issues.
  
To run the program on a local machine, compile and run the python file runserver.py

##	Basic overview about the functionality achieved

After creating an account, using Google Maps API, the location of the user is used to determine what building (if any) the user is in. If not in a building the user cannot answer any questions. The user gets a base session of 5 questions per building per day. This is to encourage the user to not only explore the campus, but to answer questions outside their major and comfort zone in order to help their team. If the If the building is neutral (no team owns it) the building will be set to a base score of 5 points and captured by the team of the first person to answer a question correctly. If the building currently has an owner, the points on the building will decrement by 1 point per question as opposing teams answer questions correctly, and increment by 1 point per question as the current owner’s team answers questions correctly. Currently you can view the top scorers on the leaderboard page, and search through each team to see player’s profiles. When playing the game, a map is present showing an icon on your current location, and every building that has questions associated with them bordered. Each building will be colored either blue (unclaimed) or the corresponding teams color. The buildings color’s transparency will change as the score of the building becomes closer to 0 or max points.

##	Future design implementation

In the future, more questions (including true or false) will be added along with the ability to select different difficulty of questions for the chance to earn more than 5 points in the session the user gets per day. 
Also an update to the questions and building JSON file implementing the enum associated with each major instead of hard coding literal numbers. 

##	Major bottlenecks

Hosting the server so that the game is live instead of on a local machine. 
Learning socketIO

