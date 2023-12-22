from pyparsing import Word, alphas,alphanums, SkipTo ,nums, delimitedList,Group, Optional, Suppress, Literal

# Değişken adı için alfa karakterleri kullanabiliriz
identifier = Word(alphanums)

# Sayısal değerler için
integer = Word(nums)

# Anahtar kelimeler
fnc_keyword = Literal("fnc")
public_keyword = Literal("public")
static_keyword = Literal("static")

# Fonksiyon parametreleri
args = Group(delimitedList(identifier))

# Geri dönüş tipi
return_type = Optional(identifier)

# Public ve static anahtar kelimeleri
public = Optional(public_keyword)
static = Optional(static_keyword)

function_content = Optional(Word(alphanums))

# Fonksiyonun gövdesi
function_body = Suppress("{") + function_content + Suppress("}")
# Test input
test_input = "fnc print (arg, arg, arg) string public static {  }"

# Parse the input
try:
    parsed = (fnc_keyword("fnc") + identifier("name") + Suppress("(") + args("args") + Suppress(")") +
              return_type("return_type") + public("public") + static("static") +
              function_body("body")).parseString(test_input)

    # Print the parsed values
    print("Function name:", parsed.name)
    print("Function arguments:", parsed.args.asList())
    print("Return type:", parsed.return_type)
    print("Public:", bool(parsed.public))
    print("Static:", bool(parsed.static))
    print("Function body:", parsed.body)
except Exception as e:
    print("Error:", e)