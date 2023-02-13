from .db import eager_find_all_tasks, eager_find_all_boards

def tasks_resolver(obj, info):
    tasks = eager_find_all_tasks()
    return tasks

def boards_resolver(obj, info):
    boards = eager_find_all_boards()
    return boards