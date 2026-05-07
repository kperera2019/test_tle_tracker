from flask import Flask
import requests
import httpx
app = Flask(__name__)

QUERY_URL="https://api.wheretheiss.at/v1/satellites/25544"


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/query")
def query():
    response = requests.get(QUERY_URL)
    return response.json()