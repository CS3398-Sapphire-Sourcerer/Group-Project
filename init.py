import flask
import flask_sqlalchemy

app = flask.Flask(__name__)
app.config.from_pyfile('settings.py')
datab = flask_sqlalchemy.SQLAlchemy(app)
