import ply.lex as lex
'''
while(conditional){ pr("HELLO WORLD"); }
'''

# Token listesi
tokens = ['WHILE', 'LPAREN', 'RPAREN', 'NUMBER', 'EQUALS', 'VARIABLE', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'SEMICOLON', 'STRING']

# Token tanımları
t_WHILE = r'while'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'==|<|>|<=|>=|!=|and|or|not'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_STRING = r'".*?"'

# Sayısal değerlerin tanımlanması
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Değişkenlerin tanımlanması
def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value not in ("while","and","not","or"):
        return t
    elif t.value == "while":
        t.type = "WHILE"
        return t
    elif t.value == "and" or t.value == "or" or t.value == "not":
        t.type = "EQUALS"
        return t
        
        

# Identifier'ın tanımlanması
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*\(\)'
    return t

# Token dışındaki karakterlerin yok sayılması
t_ignore = ' \t\n'

# Hata durumunda hata mesajı
def t_error(t):
    print(f"Geçersiz karakter: {t.value[0]}")
    t.lexer.skip(1)


# Test için örnek bir fonksiyon tanımı
def test(data):
    lexer = lex.lex()
    lexer.input(data)
    for tok in lexer:
        print(tok)

def lexWhileLoop(data):
    lexer = lex.lex()
    lexer.input(data)
    return lexer

data = 'while(500 < x and 250 == y){  }'

test(data)





