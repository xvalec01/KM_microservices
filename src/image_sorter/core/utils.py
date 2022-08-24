import json
import logging


def is_json(string):
    string = string.__str__()
    try:
        json.loads(string)
    except ValueError as e:
        return False
    return True


def jsonify(string):
    if is_json(string):
        return json.dumps(string)
