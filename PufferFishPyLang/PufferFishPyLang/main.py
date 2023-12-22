from Libraries.MathPF import MathPFloader
from Libraries.OutputPF import printClrzd
from Libraries.IntegerPF import IntegerPF
from colorama import Fore

integers = []

def findInteger(name :str) -> int:
    global integers
    for n in integers:
        if n.var_name == name:
            return n.value
    print("!ERROR! INTEGER VALUE IS INCORRECT!")        
    return None

find = False

def main():
    global find,integers
    cmd = ""
    while cmd not in ("q","quit","exit","bye"):
        cmd = input('<$>:')
        print(cmd)
        if cmd == "find":
            find = True

        splitted = cmd.split(',')

        if find == False:
            integers.append(IntegerPF(splitted[0],int(splitted[1])))
            print(integers[0])
        else:
            print(findInteger(cmd))

#Pyparsing,ANTLR,Parsimonious,ply
if __name__ == "__main__":
    printClrzd("<PufferFishPy 1.0.0>",Fore.LIGHTGREEN_EX)
    main()
    print(".")