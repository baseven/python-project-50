def get_node(old_file: dict, new_file: dict, key: str) -> dict:
    # TODO: need to come up with another way to define the type
    old_value = old_file.get(key, 'value not found')
    new_value = new_file.get(key, 'value not found')

    if old_value == 'value not found':
        return {'key': key, 'type': 'added', 'value': new_value}
    elif new_value == 'value not found':
        return {'key': key, 'type': 'deleted', 'value': old_value}
    elif isinstance(old_value, dict) and isinstance(new_value, dict):
        return {'key': key,
                'type': 'nested',
                'children': build_ast(old_value, new_value)
                }
    elif old_value == new_value:
        return {'key': key, 'type': 'unchanged', 'value': old_value}
    return {
        'key': key,
        'type': 'changed',
        'old_value': old_value,
        'new_value': new_value
    }


def build_ast(first_file: dict, second_file: dict) -> list:
    keys = sorted(set(first_file.keys()) | set(second_file.keys()))
    return [
        get_node(first_file, second_file, key)
        for key in keys
    ]
