from init import app, datab


class User(datab.Model):
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True)
    user_name = datab.Column(datab.String(20))
    pass_word = datab.Column(datab.string(64))
    q_num_answered = datab.Column(datab.Integer)
    Score = datab.Column


class Question(datab.Model):
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True)
    q_text = datab.Column(datab.String(5000))
    q_type = datab.Column(datab.Integer)
    q_value = datab.Column(datab.Integer)
    #some sort of counter to make sure its not asked multiple times in a row.
    #bld_loc = datab.Column() # this should store bld GEO data

class Team(datab.Model):
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True)
    name = datab.Column(datab.String(30))
    user = datab.Column(datab.Integer, datab.ForeignKey('user.id'))


class Building(datab.Model):
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True)
    owner = datab.Column(datab.Integer) # this holds team ID for th team owner
    #cords = datab.Column()
