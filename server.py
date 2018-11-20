from flask import Flask
app = Flask(__name__)

@app.route("/")
def getIndex():
  return "Hello World"
