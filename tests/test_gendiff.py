from gendiff.diff_generator import generate_diff
from tests.fixtures.test_result import get_test_result


def test_generate_diff_stylish():
    test_result = get_test_result('stylish')
    result_from_json = generate_diff(
        first_file_path='tests/fixtures/input_data/JSON/file1.json',
        second_file_path='tests/fixtures/input_data/JSON/file2.json')
    assert result_from_json == test_result
    result_from_yaml = generate_diff(
        first_file_path='tests/fixtures/input_data/YAML/file1.yml',
        second_file_path='tests/fixtures/input_data/YAML/file2.yml')
    assert result_from_yaml == test_result


def test_generate_diff_plain():
    test_result = get_test_result('plain')
    result_from_json = generate_diff(
        first_file_path='tests/fixtures/input_data/JSON/file1.json',
        second_file_path='tests/fixtures/input_data/JSON/file2.json',
        output_format='plain')
    assert result_from_json == test_result
    result_from_yaml = generate_diff(
        first_file_path='tests/fixtures/input_data/YAML/file1.yml',
        second_file_path='tests/fixtures/input_data/YAML/file2.yml',
        output_format='plain')
    assert result_from_yaml == test_result


def test_generate_diff_json():
    test_result = get_test_result('json')
    result_from_json = generate_diff(
        first_file_path='tests/fixtures/input_data/JSON/file1.json',
        second_file_path='tests/fixtures/input_data/JSON/file2.json',
        output_format='json')
    assert result_from_json == test_result
    result_from_yaml = generate_diff(
        first_file_path='tests/fixtures/input_data/YAML/file1.yml',
        second_file_path='tests/fixtures/input_data/YAML/file2.yml',
        output_format='json')
    assert result_from_yaml == test_result
