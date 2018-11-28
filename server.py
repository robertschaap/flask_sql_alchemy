from flask import Flask
from database import init_db, db_session

app = Flask(__name__)
init_db()

@app.route("/")
def getIndex():
  return "Hello World"

@app.teardown_appcontext
def shutdown_session(exception=None):
  db_session.remove()
