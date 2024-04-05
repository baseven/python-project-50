import argparse
from gendiff.diff_generator import generate_diff


def setup_parser():
    """Sets up the command line parser"""
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f',
                        '--format',
                        default='stylish',
                        help='set format of output')
    args = parser.parse_args()
    return args


def main():
    args = setup_parser()
    diff = generate_diff(first_file_path=args.first_file,
                         second_file_path=args.second_file,
                         output_format=args.format)
    print(diff)


if __name__ == '__main__':
    main()
