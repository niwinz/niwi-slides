all: doc
doc:
	asciidoctor -T backend/templates/haml -o index.html content.adoc

serve:
	python -m http.server 8000

watch:
	bash ./watch.sh
