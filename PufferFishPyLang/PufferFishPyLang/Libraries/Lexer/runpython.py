import ply.lex as lex
'''
PYTHON {
def prnt():
    print("hello world!")

prnt()
}
'''
tokens = ["PYTHON","LBRACE","RBRACE"]

t_PYTHON = r'PYTHON'
t_LBRACE = r'{'
t_RBRACE = r'}'

t_ignore = ' \t\n'


def t_error(t):
    print("Geçersiz karakter: %s" % t.value[0])
    t.lexer.skip(1)

# Lexer'ımızı oluşturuyoruz
lexer = lex.lex()

# Test etmek için
input_string = "PYTHON {    }"
lexer.input(input_string)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)