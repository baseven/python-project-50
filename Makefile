install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=src --cov-report xml

gendiff:
	poetry run gendiff $(first_file) $(second_file)

gendiff-json:
	poetry run gendiff tests/fixtures/JSON/file1.json tests/fixtures/JSON/file2.json

gendiff-yaml:
	poetry run gendiff tests/fixtures/YAML/file1.yml tests/fixtures/YAML/file2.yml

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 src

selfcheck:
	poetry check

check: selfcheck test lint

package-update: lint build publish package-install

.PHONY: install test lint selfcheck check build