import ply.lex as lex

tokens = ['COMMENT']

t_ignore = ' \t\n'

def t_COMMENT(t):
    r'//.*'
    t.lexer.lineno += t.value.count('\n')
    return t

def t_error(t):
    print(f"Geçersiz karakter: {t.value[0]}")
    t.lexer.skip(1)

def test(data):
    lexer = lex.lex()
    lexer.input(data)
    for tok in lexer:
        print(tok)

data = "//comment"

test(data)