# TODO: store the result not in Python files
from tests.fixtures.test_result.json import result as json_result
from tests.fixtures.test_result.plain import result as plain_result
from tests.fixtures.test_result.stylish import result as stylish_result


def get_test_result(output_format):
    formatters = {
        'stylish': stylish_result,
        'plain': plain_result,
        'json': json_result
    }
    return formatters.get(output_format, stylish_result)
