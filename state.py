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

    #state = obj

    # add all of the buildings from the DB to the state object
    app.logger.info("Made it into the function")
    app.logger.info(state)
    req = yield
    app.logger.info("Made it past")
    app.logger.info(req)

    while req is not None:
        app.logger.info("Made it into the loop")
        app.logger.info(req)
        if req['type'] == "new":
            app.logger.info("type is new")
            req = yield state
        if req['type'] == "delta":
            app.logger.info("type of request is delta")
            #'type':'delta', 'buildingTag': buildingTag, 'owner': bld.owner, 'scoreChange': scoreChange})
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
    print("Game is sending:")

    response = game.send(req)
    return response


def updateState(req):
    response = game.send(req)
    app.logger.info(response)
    return response
