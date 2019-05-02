import json
import flask
from flask import jsonify, request
from urllib.parse import urljoin

app = flask.Flask(__name__)
app.config["DEBUG"] = False

APP_URL_PREFIX = '/api/leapp-data/'

with open('test.json', 'r') as fo:
    test = json.load(fo)

@app.route(urljoin(APP_URL_PREFIX, 'test.json'), methods=['GET'])
def get_reports():
    return jsonify(test)

app.run()
