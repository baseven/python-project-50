import argparse
import json


def setup_parser():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args


def generate_diff(file_path1, file_path2):
    # TODO: Add contex manager for loading
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    keys = sorted(list(set(file1.keys()) | set(file2.keys())))

    # TODO: Take out a function
    def get_diff_line(item):
        if item not in file1:
            return f'+ {item}: {file2.get(item)}'
        elif item not in file2:
            return f'- {item}: {file1.get(item)}'
        elif file1.get(item) == file2.get(item):
            return f'  {item}: {file1.get(item)}'
        return f'- {item}: {file1.get(item)}/n+ {item}: {file2.get(item)}'

    diff_lines = [get_diff_line(item) for item in keys]
    result = '{{/n{}/n}}'.format('/n'.join(diff_lines))
    return result


def main():
    args = setup_parser()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
