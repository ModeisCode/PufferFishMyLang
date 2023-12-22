import re
TEXT = """"""

variable_section = {"variables" : [],"variable_positions" : [] , "variable_count" : 0 }

FUNCTION_COUNT = 0
FUNCTION_POSITONS = []
FUNCTIONS = []

function_section = {"functions" : [], "function_positions" : []}

COMMENT_COUNT = 0
COMMENT_POSITONS = []
COMMENTS = []

def getText(text :str):
    global TEXT
    TEXT = text

def getVariablesFromText():
    global TEXT,VARIABLE_COUNT,VARIABLE_POSITONS,VARIABLES
    splittedText = TEXT.split("\n")
    for text in splittedText:
        if (text.split(" ")[0] == "var") or (text.split(" ")[0] == "const"):
            variable_section["variable_count"] += 1

test_input = """
// variables
var char name : 'A';
var int name : 50;
var arr(int) name : {25,56,89,45};
var long name : 9999999;
var str name : "hello world";
var byte name : b"0x00";
// const variable
const var int name : 50;
"""

getText(test_input)
getVariablesFromText()
print(variable_section["variable_count"])