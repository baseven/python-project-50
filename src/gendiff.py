import argparse
from src.file_parser import get_file_parser
from src.utils import generate_diff_line, get_file_extension


def setup_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f',
                        '--format',
                        help='set format of output')
    args = parser.parse_args()
    return args


def generate_diff(file_path1, file_path2):
    file_extension = get_file_extension(file_path1)
    file_parser = get_file_parser(file_extension)

    try:
        file1 = file_parser(file_path1)
        file2 = file_parser(file_path2)
    except FileNotFoundError:
        return "Один из файлов не найден"

    keys = sorted(set(file1.keys()) | set(file2.keys()))

    indent = ' ' * 2
    diff_lines = [
        generate_diff_line(file1, file2, item, indent)
        for item in keys
    ]
    result = '{\n' + '\n'.join(diff_lines) + '\n}'
    return result


def main():
    args = setup_parser()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
