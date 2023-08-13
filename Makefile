install:
	poetry install

test:
	poetry run pytest

gendiff:
	poetry run gendiff

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