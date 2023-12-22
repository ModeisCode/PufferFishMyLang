import collections
from functions import FunctionPF

FUNCTIONS = []

def AddNewFunction(name : str,access_modifier : str , static_modifier :str,code :str):
    global FUNCTIONS
    function = FunctionPF(name,access_modifier,static_modifier,code)
    FUNCTIONS.append(function)



