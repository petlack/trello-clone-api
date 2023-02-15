import secrets
import string

db_tasks = [
    {'id': '1', 'description': 'Add GraphQL interface', 'badge': 'feature', 'board_id': '3', 'position': 0 },
    {'id': '2', 'description': 'Add functionality', 'badge': 'feature', 'board_id': '2', 'position': 0 },
    {'id': '3', 'description': 'Persistence', 'badge': 'feature', 'board_id': '1', 'position': 0 },
    {'id': '4', 'description': 'Eager/lazy loading', 'badge': 'feature', 'board_id': '1', 'position': 1 },
]

db_boards = [
    {'id': '1', 'title': 'Todo' },
    {'id': '2', 'title': 'In Progress' },
    {'id': '3', 'title': 'Done' },
]

def generate_id(length=8):
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))

def find_task(task_id):
    global db_tasks
    res = [rec for rec in db_tasks if rec['id'] == task_id]
    if not res:
        return None
    return res[0]

def find_board(board_id):
    global db_boards
    res = [rec for rec in db_boards if rec['id'] == board_id]
    if not res:
        return None
    return res[0]

def find_board_tasks(board_id):
    global db_tasks
    res = [
        rec
        for rec in db_tasks
        if rec['board_id'] == board_id
    ]
    return res

def eager_find_all_boards():
    global db_boards
    return [{**board, 'tasks': find_board_tasks(board['id']) } for board in db_boards]

def eager_find_all_tasks():
    global db_tasks
    return [{**task, 'board': find_board(task['board_id']) } for task in db_tasks]

def create_board(title):
    global db_boards

    board_id = generate_id()

    board = {
        'id': board_id,
        'title': title,
    }

    db_boards += [board]

    return board

def create_task(board_id, description, badge):
    global db_tasks

    board = find_board(board_id)
    task_id = generate_id()
    position = len(find_board_tasks(board_id))
    
    task = {
        'id': task_id,
        'description': description,
        'badge': badge,
        'board_id': board_id,
        'position': position,
    }
    db_tasks += [task]

    return {
        **task,
        'board': board,
    }

def move_task(board_id, task_id, position):
    task = find_task(task_id)
    old_board_tasks = sorted(filter(lambda rec: rec['id'] != task_id, find_board_tasks(task['board_id'])), key=lambda rec: rec['position'])
    new_board_tasks = sorted(find_board_tasks(board_id), key=lambda rec: rec['position'])

    for pos, t in enumerate(old_board_tasks):
        t['position'] = pos

    for t in new_board_tasks:
        if t['position'] >= position:
            t['position'] += 1

    task['board_id'] = board_id
    task['position'] = position

    return {
        **task,
        'board': find_board(board_id),
    }

def delete_task(task_id):
    global db_tasks
    task = find_task(task_id)
    old_board_tasks = sorted(filter(lambda rec: rec['id'] != task_id, find_board_tasks(task['board_id'])), key=lambda rec: rec['position'])
    for pos, t in enumerate(old_board_tasks):
        t['position'] = pos
    db_tasks = [t for t in db_tasks if t['id'] != task_id]
    return task
