env:
	python3 -m venv env && . env/bin/activate && pip install -U pip && pip install mkdocs mkdocs-material pymdown-extensions

serve: env
	. env/bin/activate && mkdocs serve

publish: env
	. env/bin/activate && mkdocs gh-deploy

upload-img:
	aws --profile slinjhu s3 sync --acl public-read --exclude .DS_Store img s3://sen-notes/img
	@echo "Files available as https://sen-notes.s3.us-west-2.amazonaws.com/img/*"