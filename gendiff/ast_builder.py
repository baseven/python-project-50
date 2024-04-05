def get_node(old_file, new_file, key):
    old_value = old_file.get(key)
    new_value = new_file.get(key)

    if old_value is None:
        return {'key': key, 'type': 'added', 'value': new_value}
    elif new_value is None:
        return {'key': key, 'type': 'deleted', 'value': old_value}
    elif old_value == new_value:
        return {'key': key, 'type': 'unchanged', 'value': old_value}
    return {
        'key': key,
        'type': 'changed',
        'old_value': old_value,
        'new_value': new_value
    }


def build_ast(first_file, second_file):
    keys = sorted(set(first_file.keys()) | set(second_file.keys()))
    return [
        get_node(first_file, second_file, key)
        for key in keys
    ]
