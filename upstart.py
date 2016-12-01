# This file is for all the functions that
# need to be initialized on server start
import models
from init import datab


def populate_teams():
    query = models.Teams.query.first()
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
