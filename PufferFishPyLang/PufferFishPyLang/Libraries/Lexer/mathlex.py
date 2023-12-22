import ply.lex as lex
import ply.yacc as yacc

'''
(10 + (20/2)*3)/5 
'''

tokens = ['NUMBER','PLUS','MINUS','TIMES','DIVIDE','LPAREN','RPAREN']

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = float(t.value)
    return t

def t_error(t):
    print(f"Geçersiz karakter: {t.value[0]}")
    t.lexer.skip(1)   

t_ignore = ' \t'

lexer = lex.lex()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

# Parser fonksiyonları
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_group(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_factor_uminus(p):
    'factor : MINUS factor %prec UMINUS'
    p[0] = -p[2]

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Parser oluşturma
parser = yacc.yacc()

# İfadeyi analiz etme
result = parser.parse('(25+ 50)*(2/2)')

print(result)

def test(data):
    lexer = lex.lex()
    lexer.input(data)
    for tok in lexer:
        print(tok)

data = "(25+ 50)*(2/2)"

#test(data)