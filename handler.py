from ariadne import graphql_sync
from schema import schema

def handle_graphql_request(data, context_value=None, debug=False):
    success, result = graphql_sync(
        schema,
        data,
        context_value=context_value,
        debug=debug
    )
    
    status_code = 200 if success else 400
    return result, status_code