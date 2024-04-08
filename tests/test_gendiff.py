from gendiff.diff_generator import generate_diff
from tests.fixtures.diff import flat_result, nested_result


def test_generate_diff_flat_json():
    diff = generate_diff(first_file_path='tests/fixtures/JSON/flat/file1.json',
                         second_file_path='tests/fixtures/JSON/flat/file2.json')
    assert diff == flat_result


def test_generate_diff_flat_yml():
    diff = generate_diff(first_file_path='tests/fixtures/YAML/flat/file1.yml',
                         second_file_path='tests/fixtures/YAML/flat/file2.yml')
    assert diff == flat_result


def test_generate_diff_nested_json():
    diff = generate_diff(first_file_path='tests/fixtures/JSON/nested/file1.json',
                         second_file_path='tests/fixtures/JSON/nested/file2.json')
    assert diff == nested_result


def test_generate_diff_nested_yml():
    diff = generate_diff(first_file_path='tests/fixtures/YAML/nested/file1.yml',
                         second_file_path='tests/fixtures/YAML/nested/file2.yml')
    assert diff == nested_result
