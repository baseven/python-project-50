from itertools import chain


def stringify_primitive_value(value):
    special_values = {
        'True': 'true',
        'False': 'false',
        'None': 'null'
    }
    str_value = str(value)
    return special_values.get(str_value, str_value)


def stringify(value, replacer, spaces_count, depth):
    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return stringify_primitive_value(current_value)

        indent1 = replacer * spaces_count * depth
        indent2 = replacer * spaces_count * (depth - 1)

        lines = []
        for key, val in current_value.items():
            lines.append(f'{indent1}{key}: {iter_(val, depth + 1)}')
        result = chain("{", lines, [indent2 + "}"])
        return '\n'.join(result)

    return iter_(value, depth)


def format_diff_line(
        entry: dict,
        replacer: str,
        spaces_count: int,
        depth: int,
) -> str:
    key = entry['key']
    diff_type = entry['type']
    indent = (spaces_count * depth - 2) * replacer

    if diff_type == 'added':
        value = stringify(
            value=entry["value"],
            replacer=replacer,
            spaces_count=spaces_count,
            depth=depth + 1)
        return f'{indent}+ {key}: {value}'
    elif diff_type == 'deleted':
        value = stringify(
            value=entry["value"],
            replacer=replacer,
            spaces_count=spaces_count,
            depth=depth + 1)
        return f'{indent}- {key}: {value}'
    elif diff_type == 'unchanged':
        value = stringify(
            value=entry["value"],
            replacer=replacer,
            spaces_count=spaces_count,
            depth=depth + 1)
        return f'{indent}  {key}: {value}'
    elif diff_type == 'changed':
        old_value = stringify(
            value=entry["old_value"],
            replacer=replacer,
            spaces_count=spaces_count,
            depth=depth + 1)
        new_value = stringify(
            value=entry["new_value"],
            replacer=replacer,
            spaces_count=spaces_count,
            depth=depth + 1)
        return (f'{indent}- {key}: {old_value}\n'
                f'{indent}+ {key}: {new_value}')
    stylish_diff = gen_stylish_diff(diff=entry["children"],
                                    replacer=replacer,
                                    spaces_count=spaces_count,
                                    depth=depth)
    return f'{indent}  {key}: {stylish_diff}'


def gen_stylish_diff(
        diff: list,
        replacer: str = ' ',
        spaces_count: int = 4,
        depth: int = 0,
) -> str:
    lines = [
        format_diff_line(entry, replacer, spaces_count, depth + 1)
        for entry in diff
    ]
    indent = replacer * spaces_count * depth
    result = chain("{", lines, [indent + "}"])
    return '\n'.join(result)
