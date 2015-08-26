clean:
	@find . -type d -name __pycache__ | xargs rm -rvf
	@rm -vf ../parser.out ../parsetab.py

devlexer: clean
	@cd .. && python3 -m pseudoParser.lexer pseudoParser/devel.src ; cd - >/dev/null

devparser: clean
	@cd .. && python3 -m pseudoParser pseudoParser/devel.src ; cd - >/dev/null

.PHONY: clean devlexer devparser
