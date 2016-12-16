# Group-Project
##	About the project

This project is a location-based, territory controlled, trivia game that allows Texas State University students to do the following:
* Create a profile 
* Select one of three teams (based on University school colors)
* Answer trivia questions based on the majors (i.e. Computer Science, English, Nursing, etc.) who occupy the building  

##	Team members

Adam Garcia, Brittany Torelli, Casey Sledge, Claudia Ortiz, Collin Weir, Jeremiah Burks, Kaleb Jacobson

## Neccessary Libraries

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
 
You  will additionally need to aquire a google API key for the maps access. The key can be inputed inside the api file. This key is unique to whoever is using this project. Additionally, all clients will need the SocketIO.js library, version 1.4.5, available at socket.io/download, or by using the source below in the client page:
  
  * https://cdn.socket.io/socket.io-1.4.5.js
  
## Deployment
There are several different methods to get the project running. 

To running the project in the command line, you must run the command:
python3 runserver.py socketserver 
 
To run the server in pycharm:
Right click on the runserver.py, click run, then edit the configuration and type in socketserver 
 
Both of these methods will host the project locally at 127.0.0.1:8000 or alternatively you can check your IP address on a termimal and use that IP along with the port 8000 to connect your server.

If you are going to host on a server and want it to be accessible on the internet, you need to set up a dns service to point at your servers IP and then run the app locall on the server and use a utility like gunicorn to pass socket connections to the local app.
 
 The documentation for Flask-SocketIO is a great resource for knowing how to host your production ready app and how to scale the architecture to manage load balancing and other at scale issues.
  
To run the program on a local machine, compile and run the python file runserver.py

For new installations, running the server will create and populate the database backend using specified JSON files for hard-coded information. These source files include coordinates for the buildings you wish to represent on the map, a starter set of questions and their answers, and the basic state of the game. For demonstration purposes the state file (state.json) shows some buildings as occupied by various teams. This behavior can be controlled by deleting the database, changing the buildingScore and buildingOwner values of the building to 0, and restarting the server. 


## Overview / Features

Once the server is configured and running, players may join the game by creating an account at your_hostname/signup. The player will then be redirected to the your_hostname/app page. The application page loads a static Google Map centered on the Texas State University campus, which then queries for the current owner and score on all of the nearby buildings as well as the user's location. This lookup query occurs every 15 seconds. If the user's location is found, and that location is found to be inside of a building on the Texas State University campus, the user may begin to answer questions in order to capture the building for their team. If not, the player may not answer any questions at that time. 

All players are allowed 1 session of 5 questions per building per day. This is to encourage the user to not only explore the campus, but to answer questions outside of their academic major and comfort zone in order to further their team. Buildings are captured by scoring points; points are earned by answering trivia questions associated with the building the player is in. If the building the player is in is uncaptured by a team, the first correct answer for that building receives bonus points.  Otherwise, the building's score increases by 1 if the player is on the team that owns the building, and decreases by one if the player is on one of the other two teams. If a building reaches a score of 0 it becomes unclaimed, and the first correct answer will capture the building.

Currently you can view the top scorers on the leaderboard page, and search through each team to see player’s profiles. When playing the game, a map is present showing an icon on your current location, and every building that has questions associated with them bordered. Each building will be colored either blue (unclaimed) or the corresponding teams color. The buildings color’s transparency will change as the score of the building becomes closer to 0 or max points.

##	Looking forward

We plan to add more questions, which will including true or false. As well as add the ability to select the level of difficulty of the questions for the chance to earn more than 5 points in the session the user gets per day. 
Also an update to the questions and building JSON file implementing the enum associated with each major instead of hard coding literal numbers. 

##	Major bottlenecks

Hosting the server so that the game is live instead of on a local machine. 
Learning socketIO


##	Additional Tools and Frameworks that were utilized

* Slack - communication platform for team
* PyCharm - integrated with GitHub and Slack
* Zenhub - to track groups work progress
* Pure-CSS - used for applications webpages
* Google Maps JavaScript API - used for mapping each user
* JQuery - for integrating webpages
* Bootstrap

 
