from ariadne import convert_kwargs_to_snake_case
from .db import (
    create_task,
    move_task,
)

@convert_kwargs_to_snake_case
def create_task_resolver(obj, info, board_id, description, badge):
    payload = create_task(board_id, description, badge)
    return payload

@convert_kwargs_to_snake_case
def move_task_resolver(obj, info, board_id, task_id, position):
    payload = move_task(board_id, task_id, position)
    return payload
