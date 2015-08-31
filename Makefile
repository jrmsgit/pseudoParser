clean:
	@find . -type d -name __pycache__ | xargs rm -rvf
	@rm -vf lib/parser.out lib/parsetab.py

devel.src-parse: clean
	@cd lib && python3 -m pseudoParser.parser ../devel.src ; cd - >/dev/null

devel.src-compile:
	@cd lib && python3 -m pseudoParser.compiler ../devel.src ; cd - >/dev/null

devel.src-interpreter:
	@cd lib && python3 -m pseudoParser.interpreter ../devel.src ; cd - >/dev/null

devel.src-run:
	@cd lib && python3 -m pseudoParser ../devel.src 2>/dev/null ; cd - >/dev/null

run-tests:
	@python3 -m tests 2>/dev/null

run-tests-debug:
	@python3 -m tests

.PHONY: clean devel.src-parse devel.src-compile devel.src-interpreter devel.src-run run-tests run-tests-debug
