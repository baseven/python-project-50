from src.gendiff import generate_diff
from tests.fixtures.diff import result


def test_generate_diff():
    diff = generate_diff(file_path1='tests/fixtures/file1.json',
                         file_path2='tests/fixtures/file2.json')
    assert diff == result
