from ariadne import convert_kwargs_to_snake_case
from .db import (
    create_task,
    move_task,
    delete_task,
    create_board,
)

@convert_kwargs_to_snake_case
def create_board_resolver(obj, info, title):
    payload = create_board(title)
    return payload

@convert_kwargs_to_snake_case
def create_task_resolver(obj, info, board_id, description, badge=None):
    payload = create_task(board_id, description, badge)
    return payload

@convert_kwargs_to_snake_case
def move_task_resolver(obj, info, board_id, task_id, position):
    payload = move_task(board_id, task_id, position)
    return payload

@convert_kwargs_to_snake_case
def delete_task_resolver(obj, info, task_id):
    payload = delete_task(task_id)
    return payload