import ply.lex as lex
# var char name : 'A';



tokens = (
    'VAR',
    'TYPE',
    'IDENTIFIER',
    'COLON',
    'CHARACTER',
    'INTEGER',
    'FLOAT',
    'STRING',
    'BYTE',
    'SEMICOLON'
)

def t_VAR(t):
    r'var'
    return t

def t_TYPE(t):
    r'(int|float|double|char|long|string)'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_COLON(t):
    r':'
    return t

def t_CHARACTER(t):
    r"'.'"
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'(\d+\.\d*|\.\d+)'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"'
    return t

def t_BYTE(t):
    r'b"[^"]*"'
    return t

def t_SEMICOLON(t):
    r';'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print("Geçersiz karakter: %s" % t.value[0])
    t.lexer.skip(1)

# Lexer'ımızı oluşturuyoruz
lexer = lex.lex()

# Test etmek için
input_string = "var int name : 'A';"
lexer.input(input_string)


varname = ""
varvalue = None


def lexvariable(variable_string : str,printable = True):
    global lexer,varname,varvalue
    lexer.input(variable_string)
    if printable:
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
            if tok.type == "IDENTIFIER":
                varname = tok.value
            if tok.type == "CHARACTER":
                varvalue = tok.value[1]
            if tok.type == "INTEGER":
                varvalue = int(tok.value)
    return lexer

def getvar():
    global varname,varvalue
    return (varname,varvalue)
