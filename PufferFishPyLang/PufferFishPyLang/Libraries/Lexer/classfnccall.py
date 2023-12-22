import ply.lex as lex
'''
INTEGER.changeStr("500");
'''
tokens = ["NAME","DOT_FUNCTION_LRBRACE_ARGS","SEMICOLON"]

t_SEMICOLON = r';'

t_ignore = ' \t\n'


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if (t.value == "class"):
        t.type = "CLASS"
    return t

def t_DOT_FUNCTION_LRBRACE_ARGS(t):
    r'\.[a-zA-Z]+\(([\w\s,]*)\)'
    return t

def t_error(t):
    print("Geçersiz karakter: %s" % t.value[0])
    t.lexer.skip(1)

# Lexer'ımızı oluşturuyoruz
lexer = lex.lex()

# Test etmek için
input_string = "myclass.getParse(var,myvar).get(helloworld);"
lexer.input(input_string)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)