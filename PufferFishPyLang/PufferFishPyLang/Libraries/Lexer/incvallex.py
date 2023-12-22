import ply.lex as lex

# Token listesi
tokens = ['NAME', 'VALUE', 'OP']

# Boşlukları atla
t_ignore = ' \t\n'


def t_VALUE(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_OP(t):
    r'<\+|<\-|<\*|<\/'
    return t

def t_error(t):
    print("Geçersiz karakter '%s'" % t.value[0])
    t.lexer.skip(1)

# Test input
test_input = "varname <* 500"

# Lexer oluştur
lexer = lex.lex()

# Parse the input
lexer.input(test_input)

# Tokenleri yazdır
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)