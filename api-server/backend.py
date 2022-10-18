import datetime
from flask import make_response, abort, jsonify, request

def date_time():
    now = datetime.datetime.now()
    response_json = jsonify({"datetime": now})
    return make_response(response_json, 200)
