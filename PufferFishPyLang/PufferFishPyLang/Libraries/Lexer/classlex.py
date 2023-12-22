import ply.lex as lex
'''
class INTEGER {

}
'''
tokens = ["CLASS","NAME","LBRACE","RBRACE"]

t_CLASS = r'class'
t_LBRACE = r'{'
t_RBRACE = r'}'

t_ignore = ' \t\n'

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if (t.value == "class"):
        t.type = "CLASS"
    return t

def t_error(t):
    print("Geçersiz karakter: %s" % t.value[0])
    t.lexer.skip(1)

# Lexer'ımızı oluşturuyoruz
lexer = lex.lex()

# Test etmek için
input_string = "class myclass { }"
lexer.input(input_string)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)