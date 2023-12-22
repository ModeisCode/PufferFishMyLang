import ply.lex as lex

tokens = [
    "IF",
    "LPAREN",
    "RPAREN",
    "LBRACE",
    "RBRACE",
    "CONDITIONAL",
]

t_IF = r"if|elseif"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACE = r"\{"
t_RBRACE = r"\}"

t_CONDITIONAL = r"\(.*?\)"

# Boşlukları atla
t_ignore = ' \t\n'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = "if (1==5) { }"

lexer.input(data)

for token in lexer:
    print(token)
