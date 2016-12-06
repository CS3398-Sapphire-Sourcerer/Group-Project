from init import app
import json

def gameState():
    req = None

    # state needs to have:
    # bldgName-
    # bldgShort-
    # bldgScore
    # bldgOwner

    state = {}
    with open('static\\state.json', 'r') as stateFile:
        state = json.load(stateFile)


    # add all of the buildings from the DB to the state object

    req = yield

    while req is not None:
        if req['type'] == "new":
            req = yield state
        if req['type'] == "delta":
            index = 0
            for i, v in enumerate(state["buildings"]): # in state["buildings"]:
                if v["buildingTag"] == req["buildingTag"]:
                    index = i
                    state["buildings"][i]["buildingScore"] += req["scoreChange"]
                    state["buildings"][i]["buildingOwner"] = req["owner"]
                    break
            req = yield state["buildings"][index]            


game = gameState()


def initializeGame():
    next(game)


def requestState(req):
    response = game.send(req)
    return response


def updateState(req):
    response = game.send(req)
    return response
