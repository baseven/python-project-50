import json


def gen_json_diff(dicts_diff: list) -> str:
    return json.dumps(dicts_diff, indent=2)
