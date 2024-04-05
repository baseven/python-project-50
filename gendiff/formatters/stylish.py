def gen_stylish_diff(diff: list) -> str:
    indent = ' ' * 2
    lines = [format_diff_line(entry, indent) for entry in diff]
    return '{\n' + '\n'.join(lines) + '\n}'


def format_diff_line(entry: dict, indent: str) -> str:
    key = entry['key']
    diff_type = entry['type']

    if diff_type == 'added':
        return f'{indent}+ {key}: {entry["value"]}'
    elif diff_type == 'deleted':
        return f'{indent}- {key}: {entry["value"]}'
    elif diff_type == 'unchanged':
        return f'{indent}  {key}: {entry["value"]}'
    return (f'{indent}- {key}: {entry["old_value"]}\n'
            f'{indent}+ {key}: {entry["new_value"]}')
