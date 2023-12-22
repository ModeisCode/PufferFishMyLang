import ply.lex as lex
'''
fnc function_name (args,args,args) <return_type> <public> <static> 
{
    pr(args);
}
'''
tokens = ['FNC', 'NAME', 'ARGS', 'RETURN_TYPE', 'ACCESS_MODIFIER', 'STATIC_MODIFIER', 'LBRACE', 'RBRACE', 'SEMICOLON']

# Token tanımları
def t_FNC(t):
    r'^(?!\s)fnc'
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == "fnc":
        t.type = "FNC"
    return t


def t_ARGS(t):
    r'\([^<>]*\)'
    if (t.value == ")"):
        t.type = "LBRACE"
    return t



def t_RETURN_TYPE(t):
    r'<<[a-zA-Z_][a-zA-Z0-9_]*>>' #r'<<[a-zA-Z_][a-zA-Z0-9_]*>>'
    return t

def t_ACCESS_MODIFIER(t):
    r'<public>|<private>'
    return t

def t_STATIC_MODIFIER(t):
    r'<static>'
    return t

def t_LBRACE(t):
    r'{'
    return t

def t_RBRACE(t):
    r'}'
    return t

def t_SEMICOLON(t):
    r';'
    return t

# Token dışındaki karakterlerin yok sayılması
t_ignore = ' \t\n'

# Hata durumunda hata mesajı
def t_error(t):
    print("Geçersiz karakter: '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def checkFunctionSyntax(function_string : str):
    pass

def lexfunction(function_string : str):
    global lexer
    lexer.input(function_string)
    return lexer

# Test için örnek bir fonksiyon tanımı
def test(data):
    lexer = lex.lex()
    lexer.input(data)
    for tok in lexer:
        print(tok.type)

data = 'fnc function_name (args,args,args) <<double>> <public> <static> { pr(args); }'

#test(data)

