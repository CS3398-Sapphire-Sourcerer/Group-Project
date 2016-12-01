# This file is for all the functions that
# need to be initialized on server start
import models
import json
from init import datab


def populate_teams():
    query = models.Team.query.first()
    if query is None:
        teams = models.Team()
        teams1 = models.Team()
        teams2 = models.Team()
        teams3 = models.Team()

        teams.name = 'Neutral'
        teams.score = 0
        datab.session.add(teams)
        teams1.name = 'Maroon'
        teams1.score = 0
        datab.session.add(teams1)
        teams2.name = 'Black'
        teams2.score = 0
        datab.session.add(teams2)
        teams3.name = 'Gold'
        teams3.score = 0
        datab.session.add(teams3)
        datab.session.commit()

    return

# need to eventually refactor the populate functions to move them into their own db file and not in views
# add route to populate the DB
# TODO add the building types into buildings.json then add sunctionallity into populate_buildings()
# TODO function so that it stores the building type
# TODO ********************************************
# TODO THIS NEEDS TO HAVE SCORE AND TEAMS SET TO 0 AND NULL
#
def populate_buildings():
    query = models.Building.query.first()
    if query is None:
        obj = None  # create an object to store json data
        # new_building = models.Building() #create object for individual building
        # new_coordinate = models.coordinate_point() #create object for coordinates

        # open json file as read only
        with open('static\\buildings.json', 'r') as building_list:
            obj = json.load(building_list)

        for build_count in obj["buildings"]:
            new_building = models.Building()
            new_building.name = build_count["buildingName"]
            new_building.capture_value = 0
            new_building.owner = 0
            new_building.type1 = build_count["major1"]
            new_building.type2 = build_count["major2"]
            new_building.building_shortcode = build_count["buildingTag"]
            #print("name: ", new_building.name)
            datab.session.add(new_building)
        datab.session.commit()  # commit the building so we have an ID associated to store with coordinates

        for build_count in obj["buildings"]:
            for coord_count in build_count["coordinates"]:
                new_coordinate = models.coordinate_point()
                #print("In coord loop")
                new_coordinate.long = coord_count["lng"]
                #print("lng: ", new_coordinate.long)
                new_coordinate.lat = coord_count["lat"]
                #print("lat: ", new_coordinate.lat)

                b = models.Building.query.filter_by(name=build_count["buildingName"]).first()
                new_coordinate.building_group = b.id
                datab.session.add(new_coordinate)
            datab.session.commit()  # commit all the coordinates at once


def populate_questions():
    query = models.Question.query.first()
    if query is None:
        obj = None  # create an object to store json data
        with open('static\\questions.json', 'r') as question_list:
            obj = json.load(question_list)

        for answer_count in obj["questionList"]:
            new_answer = models.Answer()
            new_answer.a_text = answer_count["ans_text"]
            new_answer.a_style = answer_count["ans_style"]
            new_answer.a_type = answer_count["question_type"]
            datab.session.add(new_answer)

        datab.session.commit()#commit all the answers so we have id's

        for question_count in obj["questionList"]:
            new_question = models.Question()
            new_question.q_text = question_count["question_text"]
            new_question.q_type = question_count["question_type"]
            new_question.q_value = question_count["question_value"]

            # query the db to get the specific answer based on text. returns the answer obj so we can store the id in the question
            ans = models.Answer.query.filter_by(a_text=question_count["ans_text"]).first()
            new_question.q_answer = ans.id

            datab.session.add(new_question)

        datab.session.commit() #commit all the questions