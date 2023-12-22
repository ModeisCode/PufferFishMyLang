import math

class MathPFloader:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def findres(numOperations: str) -> int:
        try:
            return eval(numOperations)
        except:
            return None