from gendiff.ast_builder import build_ast
from gendiff.file_parser import parse_file
from gendiff.formatters import get_formatter


def generate_diff(
        first_file_path: str,
        second_file_path: str,
        output_format: str,
) -> str:
    first_file = parse_file(first_file_path)
    second_file = parse_file(second_file_path)
    ast = build_ast(first_file, second_file)
    formatter = get_formatter(output_format)
    return formatter(ast)
