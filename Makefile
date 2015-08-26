clean:
	@find . -type d -name __pycache__ | xargs rm -rvf

devlexer:
	@cd .. && python3 -m pseudoParser.lexer pseudoParser/devel.src ; cd - >/dev/null

devparser:
	@cd .. && python3 -m pseudoParser pseudoParser/devel.src ; cd - >/dev/null

.PHONY: clean devlexer devparser
