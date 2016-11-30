# TODO Ask @Collin if we should have a constants.py module instead of magic literals for value sizes.

from init import app, datab


class User(datab.Model):
    __tablename__ = 'User'
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True)
    user_name = datab.Column(datab.String(20))
    user_profile_text = datab.Column(datab.String(1000))  # A short "about me" section, if we use it.
    pass_word = datab.Column(datab.String(64))
    email = datab.Column(datab.String(64))
    q_correct = datab.Column(datab.Integer)
    q_total = datab.Column(datab.Integer)
    Score = datab.Column(datab.Integer)
    team = datab.Column(datab.Integer, datab.ForeignKey('team.id'))
    building = datab.Column(datab.Integer, datab.ForeignKey('Building.id'))  # Current building the user has entered.
    major = datab.Column(datab.String(30))


class Question(datab.Model):
    __tablename__ = 'Question'
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True)
    q_text = datab.Column(datab.String(5000))
    q_type = datab.Column(datab.Integer)
    q_answer = datab.Column(datab.Integer)  # ID (int) of correct answer for question
    q_value = datab.Column(datab.Integer)  # Point value

    def serialize(self):
        return {
            'questionID': self.id,
            'questionText': self.q_text
        }


# Answers are seperated from Questions so that reals answers can populate incorrect answers by type
class Answer(datab.Model):
    __tablename__ = 'Answer'
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True);
    a_text = datab.Column(datab.String(1000))
    a_type = datab.Column(datab.Integer)
    a_style = datab.Column(datab.String(20))  # A string to store the type of style for the question.

    def serialize(self):
        return {
            'answerID': self.id,
            'answerText': self.a_text,
        }


# A question session is created for specific users, q_list_entries map to a specific user session id
class question_session(datab.Model):
    __tablename__ = 'question_session'
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True)
    user_id = datab.Column(datab.Integer, datab.ForeignKey('User.id'))
    building_id = datab.Column(datab.Integer, datab.ForeignKey('Building.id'))
    session_is_open = datab.Column(datab.Boolean)

    def serialize(self):
        return {
            'questionID': self.id,
            'userID': self.user_id,
            'buildingID': self.building_id,
            'sessionStatus': self.session_is_open
        }


class Q_List_Entry(datab.Model):
    __tablename__ = 'Q_List_Entry'
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True)
    question_key = datab.Column(datab.Integer, datab.ForeignKey('Question.id'))
    session_key = datab.Column(datab.Integer, datab.ForeignKey('question_session.id'))


class Team(datab.Model):
    __tablename__ = 'team'
    score = datab.Column(datab.Integer)
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True)


class Building(datab.Model):
    __tablename__ = 'Building'
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True)
    owner = datab.Column(datab.Integer, datab.ForeignKey('team.id'))  # this holds team ID for th team owner
    name = datab.Column(datab.String(30))
    capture_value = datab.Column(datab.Integer)
    type1 = datab.Column(datab.Integer)  # Primary major category found in building
    type2 = datab.Column(datab.Integer)  # Secondary (if any) major category found in building. Can be None.

    #add method to jump capture value up 10 points for team that captures it.

class coordinate_point(datab.Model):
    id = datab.Column(datab.Integer, primary_key=True, autoincrement=True)
    building_group = datab.Column(datab.Integer, datab.ForeignKey('Building.id'))
    long = datab.Column(datab.Integer)
    lat = datab.Column(datab.Integer)


datab.create_all(app=app)
