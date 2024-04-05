import json
import yaml


def load_json(file_path):
    with open(file_path, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error loading JSON from file '{file_path}': {e}")


def load_yaml(file_path):
    with open(file_path, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as e:
            raise ValueError(f"Error loading YAML from file '{file_path}': {e}")


def get_file_parser(file_extension):
    parsers = {
        'json': load_json,
        'yaml': load_yaml,
        'yml': load_yaml,
    }
    parser = parsers.get(file_extension.lower())
    if not parser:
        raise ValueError(f"Unsupported file extension: '{file_extension}'")
    return parser
