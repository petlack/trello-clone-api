def tasks_resolver(obj, info):
    tasks = [
        {"id": '1', "description": "Add GraphQL interface", "badge": 'feature' },
        {"id": '2', "description": "Add functionality", "badge": 'feature' },
    ]
    print(tasks)
    payload = tasks
    return payload