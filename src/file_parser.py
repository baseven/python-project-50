import json
import yaml


# TODO: Add contex manager for loading
def get_file_parser(file_format):
    if file_format == 'JSON':
        return lambda file_path: json.load(open(file_path))
    elif file_format == 'YAML':
        return lambda file_path: yaml.safe_load(open(file_path))
