#This class is meant to handle the database queries for questions and answers, as well as store the questions for one
#building session consisting of N questions.

#Usage note: After connecting session the the database, it is possible for a user to leave a session midway through and
#            return later. The question list only builds questions are are still valid and answerable, meaning the list
#            can potentially be shorter than the session length. TODO Revisit this logic if this begins causing errors.


from init import datab
from sqlalchemy import and_
from random import shuffle
import models

#This class contains easy methods for adding question-relavent database content
class q_database_manager:
    def addQuestionWithAnswer(self, questionText, questionType, answerText):
        # TODO, add verification to fields, make sure you get good data
        # Create models and fill data fields
        question = models.Question()
        current_answer = models.Answer()

        question.q_text = questionText
        question.q_type = questionType

        current_answer.a_text = answerText
        current_answer.a_type = questionType

        datab.session.add(current_answer)
        datab.session.commit()  # Save the answer and generate an ID

        question.q_answer = current_answer.id  # current_answer.id   #Pulled from model that was just commited

        datab.session.add(question)  # Save the question
        datab.session.commit()

    def addBuilding(self, new_name, new_type1):
        #TODO add support for type2, owner and coordinates
        new_building = models.Building()
        new_building.name = new_name
        new_building.type1 = new_type1

        datab.session.add(new_building)
        datab.session.commit()

class q_data:               # Used to group questions with a specifc answers list
    question = None
    answers_list = []

    def serialize(self):
        return {
            'question': self.question.serialize(),
            'answer_list': [answer.serialize() for answer in self.answers_list]
        }

class question_handler:
    SESSION_LENGTH = 5     #Max number of questions a user can answer at one building
    POTENTIAL_ANSWERS = 4  #Number of possible answers to each question, one answer is correct

    question_list = []     #List of questions for current building session
    question_session_index = 0
    session = None


    type

    def __init__ (self, user_id, building_id):

        self.session = models.question_session.query.filter(models.question_session.user_id==user_id, models.question_session.building_id==building_id).first()

        if self.session is None: #If query session does not exist, build a new session
            b = models.Building.query.get(building_id)
            self.type = b.type1                     #If you get errors, verify that this is a building object and not a standard query.
            self.question_index = 0
            self.buildNewQuestionSession(user_id, building_id)
        elif self.session.session_is_open: #If query session does exist, reopen where the user left off.
            qlist = models.Q_List_Entry.query.filter_by(session_key = self.session.id)
            workingList = list(qlist)

            if workingList is None: #No entires remain, close the session
                self.session.session_is_open = False
                datab.session.commit()
            else:
                for q_entry in workingList:
                    question = models.Question.query.filter_by(id = q_entry.question_key).first()
                    q = q_data()
                    q.question = question
                    q.answers_list = self.getPotentialtAnswers(question)
                    self.question_list.append(q)
        else:
            #The user's question session exist and is closed. Print some message saying they reached their max
            return None




    def buildNewQuestionSession(self, user_id, building_id):
        self.question_list = []
        workingList = self.getQuestions()

        if len(workingList) < self.SESSION_LENGTH:
            print("***ERROR, not enough questions in category. Enter more questions for testing or handle case with too few entries.***")
            return False
        else:
            #Build session object in database
            self.session = models.question_session()
            self.session.building_id = building_id
            self.session.user_id = user_id
            self.session.session_is_open = True

            datab.session.add(self.session)
            datab.session.commit()

            for question in workingList:
                q = q_data()
                q.question = question
                q.answers_list = self.getPotentialtAnswers(question)
                self.question_list.append(q)

                #Build one q_entry for each question and point them at the current session
                q_entry = models.Q_List_Entry()
                q_entry.question_key = question.id
                q_entry.session_key = self.session.id

                datab.session.add(q_entry)
            datab.session.commit()


    #Query database for N random questions, return list
    def getQuestions(self):
        #Get all possible questions
        q = models.Question.query.filter_by(q_type = self.type)
        questionsByType = list(q)                   #Get full list
        shuffle(questionsByType)                    #Shuffle list

        #TODO: verify size of list here, check for errors
        del questionsByType[self.SESSION_LENGTH:]   #Trim list to desired number of elements

        return questionsByType

    #Query database for list of answers, including one correct answer
    def getPotentialtAnswers(self, question):
        correctAnswer = self.getCorrectAnswer(question)

        #Get all answers that are of a specific type and NOT the correct answer
        a = models.Answer.query.filter(models.Answer.a_type == question.q_type, models.Answer.id != correctAnswer.id)
        potentialAnswers = list(a)                          #Turn into list format

        shuffle(potentialAnswers)
        del potentialAnswers[self.POTENTIAL_ANSWERS-1:]     #Save only 3 shuffled answers
        potentialAnswers.append(correctAnswer)              #Append correct answer
        shuffle(potentialAnswers)                           #Shuffle the N possible answers

        return potentialAnswers

    #Change question type, may not be needed if we simple create a new handler each time
    def setQuestionType(self, question_type):
        self.type = question_type

    #Query database for correct answer based on question
    #TODO: Update this to use forgin keys over ints
    def getCorrectAnswer(self, question):
        key = question.q_answer
        answer = models.Answer.query.filter_by(id = key).first()
        return answer

    def setQuestionIndex(self, newIndex):
        self.question_session_index = newIndex
        return None

    def nextQuestionIndex(self):
        listSize = len(self.question_list)
        self.question_session_index = self.question_session_index + 1
        if self.question_session_index >= listSize:
            self.question_session_index = 0
            q_session = models.question_session.query.get(self.session.id)
            print("****Closing session****")
            q_session.session_is_open = False
            datab.session.commit()

    def serializeCurrentQuestion(self):
        if self.question_session_index >= len(self.question_list):
            print("Error, index out of bounds")
        else:
            return{
                'question_data': self.question_list[self.question_session_index].serialize()
            }

    def serialize(self):
        return {
            'sessionLength': self.SESSION_LENGTH,
            'question_data_entries': [q_data.serialize() for q_data in self.question_list]
        }

