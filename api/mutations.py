from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def create_task_resolver(obj, info, description, badge):
    payload = {
        "id": "999",
        "description": description,
        "badge": badge,
    }
    return payload

@convert_kwargs_to_snake_case
def move_task_resolver(obj, info, id, column):
    payload = {
        "id": id,
        "column": column,
    }
    return payload

@convert_kwargs_to_snake_case
def reorder_task_resolver(obj, info, id, position):
    payload = {
        "id": id,
        "position": position,
    }
    return payload