from gendiff.formatters.json import gen_json_diff
from gendiff.formatters.plain import gen_palin_diff
from gendiff.formatters.stylish import gen_stylish_diff


def get_formatter(output_format):
    formatters = {
        'stylish': gen_stylish_diff,
        'plain': gen_palin_diff,
        'json': gen_json_diff,
    }
    return formatters.get(output_format, None)
