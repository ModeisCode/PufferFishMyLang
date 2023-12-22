from colorama import Fore,Back

def printClrzd(txt: str,Color: Fore):
    print(Color + txt + Fore.RESET)