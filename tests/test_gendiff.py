from src.gendiff import generate_diff
from tests.fixtures.diff import result


def test_generate_diff():
    diff = generate_diff(file_path1='tests/fixtures/JSON/file1.json',
                         file_path2='tests/fixtures/JSON/file2.json',
                         file_format='JSON')
    assert diff == result


def test_generate_diff_yml():
    diff = generate_diff(file_path1='tests/fixtures/YAML/file1.yml',
                         file_path2='tests/fixtures/YAML/file2.yml',
                         file_format='YAML')
    assert diff == result
