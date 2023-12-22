from Libraries.Lexer.varlex import lexvariable,varname,getvar
from Libraries.Operations.varoperations import AddIntegerVariable
from Libraries.SemanticAnalysis.varSAPF import ParseVariableSAPF
from colorama import Fore
from Libraries.OutputPF import printClrzd
test_input = "var char name : 'A';"
varlexer = lexvariable(test_input,True)
print("VARNAME:",getvar()[1])
print("VARNAME:",getvar()[0])
if ParseVariableSAPF(test_input):
    printClrzd("[OK]",Fore.LIGHTGREEN_EX)
else:
    printClrzd("[ERROR]",Fore.LIGHTRED_EX)
