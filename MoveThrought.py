from Function import Function

class MoveThrought(Function):

    def __init__(self, startState, elements, direction: int, rank=4):
        super().__init__(startState, rank)
        self.elements = elements
        self.direction = direction

    direc = "<>"
    
    def changeState(self, rank, change=None) -> str:
        return super().changeState(rank, change)

    def endState(self) -> int:
        return super().endState()
    
    def startCycle(self, change, rank=2):
        return super().startCycle(change, rank)
    
    def code(self, condition: str, action: int, change=None, startState=None, endState=None):
        return super().code(condition, action, change, startState, endState)

    def build(self, alphabet):
        self.code(" ",self.direction,1,self.startState)
        self.code(" ",self.direction)
        self.code(alphabet,2,1)
        for el in range(1, self.elements*2):
            if el%2!=0:
                self.code(alphabet,self.direction)
                self.code(" ",2 if el == self.elements * 2 - 1 else self.direction,1, endState=self.endState() if el == self.elements * 2 - 1 else None)
            else:
                self.code(" ",self.direction)
                self.code(alphabet,0 if self.direction else 1,1)
                self.code(" ",self.direction,1)
        return self.tuCode
