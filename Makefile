create-venv:
	python -m venv .venv

setup:
	pip install -r requirements.txt

clean:
	rm -rf ./**/__pycache__ __pycache__ .benchmarks htmlcov .pytest_cache
	rm -f .coverage

code-convention:
	flake8
	pycodestyle

test:
	py.test -v

test-cov:
	py.test -v --cov-report=term --cov-report=html --cov=.