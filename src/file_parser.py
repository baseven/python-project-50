import json
import yaml


def load_json(file_path):
    with open(file_path, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error loading JSON from file '{file_path}': {e}")
            return None


def load_yaml(file_path):
    with open(file_path, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(f"Error loading YAML from file '{file_path}': {e}")

            return None


def get_file_parser(file_extension):
    if file_extension == 'json':
        return lambda file_path: load_json(file_path)
    elif file_extension in ['yaml', 'yml']:
        return lambda file_path: load_yaml(file_path)
    else:
        print(f"Unsupported file extension: '{file_extension}'")
        return None
