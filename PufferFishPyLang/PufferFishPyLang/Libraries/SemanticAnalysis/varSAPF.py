from pyparsing import Word, alphas, alphanums, Literal, Suppress, oneOf

# Anahtar kelime için alfa karakterleri kullanabiliriz
var_keyword = Literal("var")
identifier = oneOf("string char int double")
variable_name = Word(alphanums)
value = Suppress(":") + Suppress("'") + Word(alphanums) + Suppress("'")
semicolon = Suppress(";") 
variable_value = var_keyword + identifier + variable_name("name") + value("value") + semicolon

# Test input
test_input = "var char name : 'A';"

# Parse the input
try:
    parsed = variable_value.parseString(test_input)
    print("Variable name:", parsed.name)
    print("Variable value:", parsed.value)
except Exception as e:
    print("Error:", e)

def ParseVariableSAPF(input) -> bool:
    global variable_value
    try:
        parsed = variable_value.parseString(input)
        print("Variable name:", parsed.name)
        print("Variable value:", parsed.value)
        return True
    except Exception as e:
        print("Error:", e)
        return False