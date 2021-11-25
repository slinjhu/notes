ENV=. env/bin/activate &&

test: env
	${ENV} python -m unittest discover -p "test_*.py"

env:
	python3 -m venv env && ${ENV} pip install -U pip wheel && pip install -r requirements.txt
