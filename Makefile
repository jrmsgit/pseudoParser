clean:
	@find . -type d -name __pycache__ | xargs rm -rvf
	@rm -vf lib/parser.out lib/parsetab.py

devlexer: clean
	@cd lib && python3 -m pseudoParser.lexer ../devel.src ; cd - >/dev/null

devparser: clean
	@cd lib && python3 -m pseudoParser ../devel.src ; cd - >/dev/null

.PHONY: clean devlexer devparser
