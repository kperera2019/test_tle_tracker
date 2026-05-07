from flask import Flask

app = Flask(__name__)

QUERY_URL="https://api.wheretheiss.at/v1/satellites/25544"


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"