templates = {
    'added': lambda path, value: (
        f"Property '{path}' was added with value: {value}"
    ),
    'deleted': lambda path: (
        f"Property '{path}' was removed"
    ),
    'changed': lambda path, old_value, new_value: (
        f"Property '{path}' was updated. From {old_value} to {new_value}"
    ),
}


def modify_string(value):
    return f"'{value}'"


def modify_bool(value):
    return 'true' if value else 'false'


def modify_value(value):
    if value is None:
        return 'null'
    elif isinstance(value, str):
        return modify_string(value)
    elif isinstance(value, bool):
        return modify_bool(value)
    elif isinstance(value, (list, dict)):
        return '[complex value]'
    return value


def format_diff_line(diff: dict, path: str = '') -> str:
    path += diff['key']

    if diff['type'] == 'added':
        return templates['added'](path, modify_value(diff['value']))
    elif diff['type'] == 'deleted':
        return templates['deleted'](path)
    elif diff['type'] == 'changed':
        old_value = modify_value(diff['old_value'])
        new_value = modify_value(diff['new_value'])
        return templates['changed'](path, old_value, new_value)
    return gen_palin_diff(diff['children'], path + '.')


def gen_palin_diff(diff: list, path: str = '') -> str:
    lines = [
        format_diff_line(entry, path)
        for entry in diff
        if entry['type'] != 'unchanged'
    ]
    return '\n'.join(lines)
