lex = None

# dictionary of names
varsTable = dict()

def p_statement_assign(p):
    "statement : NAME '=' expression ';'"
    if p[1] not in varsTable.keys():
        raise LookupError("undefined var '%s' at line '%d'" % (p[1], lex.lexer.lineno))
    varsTable[p[1]] = p[3]
