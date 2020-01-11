env:
	python3 -m venv env && . env/bin/activate && pip install -U pip && pip install mkdocs mkdocs-material pymdown-extensions

serve: env
	. env/bin/activate && mkdocs serve

publish: env
	. env/bin/activate && mkdocs gh-deploy