install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

gendiff:
	poetry run gendiff $(first_file) $(second_file)

gendiff-json-stylish:
	poetry run gendiff tests/fixtures/input_data/JSON/file1.json tests/fixtures/input_data/JSON/file2.json

gendiff-yaml-stylish:
	poetry run gendiff tests/fixtures/input_data/YAML/file1.yml tests/fixtures/input_data/YAML/file2.yml

gendiff-json-plain:
	poetry run gendiff --format plain tests/fixtures/input_data/JSON/file1.json tests/fixtures/input_data/JSON/file2.json

gendiff-yaml-plain:
	poetry run gendiff --format plain tests/fixtures/input_data/YAML/file1.yml tests/fixtures/input_data/YAML/file2.yml

gendiff-json-json:
	poetry run gendiff --format json tests/fixtures/input_data/JSON/file1.json tests/fixtures/input_data/JSON/file2.json

gendiff-yaml-json:
	poetry run gendiff --format json tests/fixtures/input_data/YAML/file1.yml tests/fixtures/input_data/YAML/file2.yml

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

package-update: lint build publish package-install

.PHONY: install test lint selfcheck check build