#This class is meant to handle the database queries for questions and answers, as well as store the questions for one
#building session consisting of N questions.

from init import datab
from sqlalchemy import and_
from random import shuffle
import models


class q_data:               # Used to group questions with a specifc answers list
    question = None
    answers_list = []

class question_handler:
    SESSION_LENGTH = 5     #Max number of questions a user can answer at one building
    POTENTIAL_ANSWERS = 4  #Number of possible answers to each question, one answer is correct

    question_list = []     #List of questions for current building session

    type

    def __init__ (self, question_type):
        self.type = question_type
        self.question_index = 0
        self.buildNewQuestionSession()

        return

    def buildNewQuestionSession(self):
        self.question_list = []
        workingList = self.getQuestions()

        for question in workingList:
            q = q_data()
            q.question = question
            q.answers_list = self.getPotentialtAnswers(question)
            self.question_list.append(q)

        for questionData in self.question_list:
            print (questionData.question.q_text)
            for answers in questionData.answers_list:
                print ("->" + answers.a_text)


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
        a = models.Answer.query.filter_by(a_type = question.q_type)
        potentialAnswers = list(a)

        shuffle(potentialAnswers)
        del potentialAnswers[self.POTENTIAL_ANSWERS-1:]        #Save only 3 shuffled answers
        print (potentialAnswers)
        potentialAnswers.append(self.getCorrectAnswer(question))  #Append correct answer
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

