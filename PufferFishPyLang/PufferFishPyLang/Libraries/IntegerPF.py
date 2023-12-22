
class IntegerPF:
    def __init__(self,name,def_value :int) -> None:
        self.var_name = name
        self.value = def_value

    @classmethod
    def toStr(self) -> str:
        return str(self.value)
    
    