install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

gendiff:
	poetry run gendiff $(first_file) $(second_file)

gendiff-json-flat:
	poetry run gendiff tests/fixtures/JSON/flat/file1.json tests/fixtures/JSON/flat/file2.json

gendiff-json-nested:
	poetry run gendiff tests/fixtures/JSON/nested/file1.json tests/fixtures/JSON/nested/file2.json

gendiff-yaml-flat:
	poetry run gendiff tests/fixtures/YAML/flat/file1.yml tests/fixtures/YAML/flat/file2.yml

gendiff-yaml-nested:
	poetry run gendiff tests/fixtures/YAML/nested/file1.yml tests/fixtures/YAML/nested/file2.yml

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