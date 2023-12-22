import ply.lex as lex
from varlex import lexvariable
from funclex import lexfunction
'''
input_string = """
var char name1 : 'A';
var int name2 : 50;
var long name4 : 9999999;
var str name5 : "hello world";
var byte name6 : b"0x00";
"""

VAR_LEXER = lexvariable(input_string,False)

while True:
    tok = VAR_LEXER.token()
    if not tok:
        break
    if tok.type == "SEMICOLON":
        print("------------")
    print(tok)  

'''

input_string = """
fnc myfunction(myarg1,myarg2,myarg3) 
{

}
"""

fnclexer = lexfunction(input_string)
getcode = False

while True:
    tok = fnclexer.token()
    if not tok:
        break
    if tok.type == "LBRACE":
        getcode = True
    #elif (getcode == True) and (tok.type != "RBRACE"):
    print(tok)
