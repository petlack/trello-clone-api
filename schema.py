from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
    ObjectType,
)

from api.queries import (
    boards_resolver,
    tasks_resolver,
    timestamp_resolver,
)

from api.mutations import (
    create_task_resolver,
    move_task_resolver,
    delete_task_resolver,
    create_board_resolver,
)

query = ObjectType("Query")
query.set_field("timestamp", timestamp_resolver)
query.set_field("tasks", tasks_resolver)
query.set_field("boards", boards_resolver)

mutation = ObjectType("Mutation")
mutation.set_field("createBoard", create_board_resolver)
mutation.set_field("createTask", create_task_resolver)
mutation.set_field("moveTask", move_task_resolver)
mutation.set_field("deleteTask", delete_task_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)