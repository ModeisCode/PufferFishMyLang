import ply.lex as lex

# Token listesi
tokens = ['NAME', 'VALUE', 'OP', 'OPTIONAL_VALUE']

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
    r'<'
    return t

def t_error(t):
    print("Geçersiz karakter '%s'" % t.value[0])
    t.lexer.skip(1)

def t_optional_value(t):
    r'\?'
    t.value = None
    return t


# Tokenlari tanimla
def t_ANY_OPTIONAL_VALUE(t):
    r'\?'
    t.type = 'OPTIONAL_VALUE'
    t.value = None
    return t

# Test input
test_input = "var_name < 500"

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