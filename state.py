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
        if req['type'] == "new":
            app.logger.info("type is new")
            app.logger.info(state)
            #yield state
            req = yield state


# generators are fucking
game = gameState()


def initializeGame():
    next(game)


def requestState(req):
    response = game.send(req)
    return response


def updateState(req):
    pass
