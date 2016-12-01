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

    # state = obj

    # add all of the buildings from the DB to the state object
    app.logger.info("Made it into the function")
    app.logger.info(state)
    req = yield
    app.logger.info("Made it past")
    app.logger.info(req)

    while req is not None:
        app.logger.info("Made it into the loop")
        if req['type'] == "new":
            app.logger.info("type is new")
            req = yield state
        if req['type'] == "delta":
            app.logger.info("type of request is delta")
            index = 0
            for i, v in enumerate(state["buildings"]):  # in state["buildings"]:
                if v["buildingTag"] == req["buildingTag"]:
                    state["buildings"][i]["buildingScore"] += req["q_result"]
                    if v["buildingOwner"] != req["owner"]:
                        state["buildings"][i]["buildingScore"] = req["owner"]
                    break
            req = yield state["buildings"][i]
            # if v["buildingTag"] == req["buildingTag"]:
            #    index =
            # if (state['buildings'].index)


# generators are fucking
game = gameState()


def initializeGame():
    next(game)


def requestState(req):
    print("Game is sending:")

    response = game.send(req)
    return response


def updateState(req):
    response = game.send(req)
    return response
