clean:
	@find . -type d -name __pycache__ | xargs rm -rvf
	@rm -vf lib/parser.out lib/parsetab.py

devparser: clean
	@cd lib && python3 -m pseudoParser.parser ../devel.src ; cd - >/dev/null

devrun: clean
	@cd lib && python3 -m pseudoParser ../devel.src ; cd - >/dev/null

.PHONY: clean devparser devrun
