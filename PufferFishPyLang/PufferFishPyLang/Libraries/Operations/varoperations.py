import collections
#var char name : 'A';

INTEGER_VARIABLES = collections.defaultdict(list)
CHAR_VARIABLES = collections.defaultdict(list)
FLOAT_VARIABLES = collections.defaultdict(list)
DOUBLE_VARIABLES = collections.defaultdict(list)
LONG_VARIABLES = collections.defaultdict(list)
STRING_VARIABLES = collections.defaultdict(list)
BYTE_VARIABLES = collections.defaultdict(list)
ARR_VARIABLES = collections.defaultdict(list)


def AddIntegerVariable(name :str , value: int):
    global INTEGER_VARIABLES
    INTEGER_VARIABLES[name].append(value)
    print(INTEGER_VARIABLES[name])

def AddCharVariable(name :str , value: chr):
    global CHAR_VARIABLES
    CHAR_VARIABLES[name].append(value)
    print(CHAR_VARIABLES[name])

