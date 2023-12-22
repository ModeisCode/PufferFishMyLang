import ast
import ply.lex as lex

code = "var int name : 50;"
code_list = ("var","int","name",":","50",";")

varlist = ["char","int","string","double","float","long"]

def getCode(code_list,SAPF : bool , lexedCorrect : bool) -> str:
    if (SAPF == True) and (lexedCorrect == True):
        if (code_list[0] == "var") and (code_list[1] in varlist) and (code_list[2][0] not in "0123456789") and (code_list[4].isnumeric()):
            new_pythonscript = code_list[2] + "=" + code_list[4]
            return new_pythonscript

def check_syntax(code):
    try:
        ast.parse(code)
        print('Syntax OK')
    except:
        print('Syntax Error:')
        