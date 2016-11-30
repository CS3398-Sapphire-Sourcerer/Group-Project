from init import app
def gameState():
    req = None

    state = dict(buildings=["derrick", "alkek"])

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
            yield state
            req = yield

game = gameState()

def initializeGame():
    next(game)

def requestState(req):
    return game.send(req)

def updateState(req):
    pass


