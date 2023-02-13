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

def find_task(task_id):
    res = [rec for rec in db_tasks if rec['id'] == task_id]
    if not res:
        return None
    return res[0]

def find_board(board_id):
    res = [rec for rec in db_boards if rec['id'] == board_id]
    if not res:
        return None
    return res[0]

def find_task_board(task_id):
    task = find_task(task_id)
    board = find_board(task['board_id'])
    return board

def find_board_tasks(board_id):
    res = [
        rec
        for rec in db_tasks
        if rec['board_id'] == board_id
    ]
    return res

def eager_find_all_boards():
    return [{**board, 'tasks': find_board_tasks(board['id']) } for board in db_boards]

def eager_find_all_tasks():
    return [{**task, 'board': find_task_board(task['id']) } for task in db_tasks]

def create_task(board_id, description, badge):
    global db_tasks

    board = find_board(board_id)
    task_id = len(db_tasks) + 1
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