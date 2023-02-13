from api import app
from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    graphql_sync,
    snake_case_fallback_resolvers,
    ObjectType,
)
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

from api.queries import (
    boards_resolver,
    tasks_resolver,
)
from api.mutations import (
    create_task_resolver,
    move_task_resolver,
)

query = ObjectType("Query")
query.set_field("tasks", tasks_resolver)
query.set_field("boards", boards_resolver)

mutation = ObjectType("Mutation")
mutation.set_field("createTask", create_task_resolver)
mutation.set_field("moveTask", move_task_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code