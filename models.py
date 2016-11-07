#TODO Ask @Collin if we should have a constants.py module instead of magic literals for value sizes.

from init import app, datab

class User(datab.Model):
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True)
    user_name = datab.Column(datab.String(20))
    pass_word = datab.Column(datab.String(64))
    email = datab.Column(datab.String(64))
    q_correct = datab.Column(datab.Integer)
    q_total = datab.Column(datab.Integer)
    Score = datab.Column(datab.Integer)
    building = datab.Column(datab.Integer, datab.ForeignKey('team.id'))



class Question(datab.Model):
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True)
    q_text = datab.Column(datab.String(5000))
    q_type = datab.Column(datab.Integer)
    q_answer = datab.Column(datab.Integer)   #ID (int) of correct answer for question
    q_value = datab.Column(datab.Integer)    #Point value
    #some sort of counter to make sure its not asked multiple times in a row.
    #bld_loc = datab.Column() # this should store bld GEO data

#Answers are seperated from Questions so that reals answers can populate incorrect answers by type
class Answer(datab.Model):
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True);
    a_text = datab.Column(datab.String(1000))
    a_type = datab.Column(datab.Integer)

class Team(datab.Model):
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True)
    name = datab.Column(datab.String(30))


class Building(datab.Model):
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True)
    owner = datab.Column(datab.Integer, datab.ForeignKey('team.id')) # this holds team ID for th team owner
    #cords = datab.Column()
    name = datab.Column(datab.String(30))
    score = datab.Column(datab.Integer)

datab.create_all(app=app)
