clean:
	@find . -type d -name __pycache__ | xargs rm -rvf
	@rm -vf lib/parser.out lib/parsetab.py

parse-devel.src: clean
	@cd lib && python3 -m pseudoParser.parser ../devel.src ; cd - >/dev/null

run-devel.src: clean
	@cd lib && python3 -m pseudoParser ../devel.src ; cd - >/dev/null

.PHONY: clean parse-devel.src run-devel.src
