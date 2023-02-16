import time 
import random

from api.app import app
from handler import handle_graphql_request

from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    time.sleep(2 * random.random());
    prob = 5 if data['operationName'] == 'BoardsQuery' else 1
    if random.randint(0, prob) == 0:
        return jsonify({ "data": None, "errors": ["Unexpected error"] }), 200
    
    result, status_code = handle_graphql_request(
        data,
        context_value=request,
        debug=app.debug,
    
    )
    return jsonify(result), status_code
    

