import datetime

from .db import eager_find_all_tasks, eager_find_all_boards

def timestamp_resolver(obj, info):
    return str(datetime.datetime.now())

def tasks_resolver(obj, info):
    tasks = eager_find_all_tasks()
    return tasks

def boards_resolver(obj, info):
    boards = eager_find_all_boards()
    return boards