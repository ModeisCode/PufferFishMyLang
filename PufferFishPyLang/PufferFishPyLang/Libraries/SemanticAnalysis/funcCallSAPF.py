from pyparsing import Word, alphas,alphanums, SkipTo ,nums, delimitedList,Group, Optional, Suppress, Literal
# function_name(args,args,args);

function_name = Word(alphanums)
args = Group(delimitedList(Word(alphanums)))
semicolon = Suppress(";")

test_input = "functionname(args,args,args);"

# Parse the input
try:
    parsed = (function_name("name") + Suppress("(") + args("args") + Suppress(")") + semicolon).parseString(test_input)
    # Print the parsed values
    print("Function name:", parsed.name)
    print("Arguments:", parsed.args.asList())
    
except Exception as e:
    print("Error:", e)



