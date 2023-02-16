import json
from ariadne.constants import PLAYGROUND_HTML

from handler import handle_graphql_request

def lambda_handler(event, context):
    if event['requestContext']['http']['method'] == 'GET':
        return {
            "body": PLAYGROUND_HTML,
            "headers": {
                "Content-Type": "text/html",
            },
            "statusCode": 200,
        }
    
    data = json.loads(event['body'])
    result, status_code = handle_graphql_request(data)
    return {
        "statusCode": status_code,
        "body": json.dumps(result),
    }