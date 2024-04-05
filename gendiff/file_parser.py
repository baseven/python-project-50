import json
import yaml
from pathlib import Path


def get_file_extension(file_path: str) -> str:
    return Path(file_path).suffix[1:].lower()


def get_file_parser(file_path: str) -> dict:
    parsers = {
        'json': {'loader': json.load,
                 'loading_error': json.JSONDecodeError},
        'yaml': {'loader': yaml.safe_load,
                 'loading_error': yaml.YAMLError},
        'yml': {'loader': yaml.safe_load,
                'loading_error': yaml.YAMLError},
    }

    file_extension = get_file_extension(file_path)
    parser = parsers.get(file_extension)
    if not parser:
        raise ValueError(f"Unsupported file extension: '{file_extension}'")
    return parser


def load_file(path: str, loader, loading_error: Exception) -> dict:
    with open(path, 'r') as file:
        try:
            return loader(file)
        except loading_error as e:
            raise ValueError(f"Error loading from file '{path}': {e}")


def parse_file(file_path: str) -> dict:
    file_parser = get_file_parser(file_path)
    return load_file(path=file_path,
                     loader=file_parser['loader'],
                     loading_error=file_parser['loading_error'])
