import os


def generate_diff_line(file1, file2, item, indent):
    value1 = file1.get(item)
    value2 = file2.get(item)

    if value1 is None:
        return f'{indent}+ {item}: {value2}'
    elif value2 is None:
        return f'{indent}- {item}: {value1}'
    elif value1 == value2:
        return f'{indent}  {item}: {value1}'
    else:
        return f'{indent}- {item}: {value1}\n{indent}+ {item}: {value2}'


def get_file_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension[1:]
