from Function import Function
from MoveThrought import MoveThrought

class CopyThrought(Function):
    def __init__(self, startState, elements, directionFrom, directionTo, rank=4):
        super().__init__(startState, rank) 
        self.elements = elements
        self.directionFrom = directionFrom
        self.directionTo = directionTo

    direc = "<>"

    def changeState(self, bias=0) -> str:
        return super().changeState(bias)
    
    def endState(self) -> int:
        return super().endState() 
    
    def build(self, alphabet):
        if self.directionFrom == 0:
            left = MoveThrought(self.startState, 1, 0)
            self.tuCode += left.build(alphabet)
            self.tuCode += f"\n{left.endState()}, ,>,{self.currState}"
            self.uses += 1
        else:
            self.tuCode += f"\n{self.startState}, ,{self.direc[self.directionFrom]},{self.currState}"
            self.tuCode += f"\n{self.currState}, ,{self.direc[self.directionFrom]},{self.currState}"
            temp = self.currState
            self.changeState(1)
            for x in alphabet:
                self.tuCode += f"\n{temp},{x},=,{self.currState}"
            for i in alphabet:
                temp1 = self.currState
                self.tuCode += f"\n{self.currState},{i}, ,{self.endState()}"
                self.tuCode += f"\n{self.currState}, ,#,{self.endState()}"
                mov = MoveThrought(self.endState(), self.elements, self.directionTo)
                self.tuCode += mov.build(alphabet)
                self.uses += 1
                self.tuCode += f"\n{mov.endState()}, ,>,{self.changeState(1)}"
                self.uses += 1
                self.tuCode += f"\n{self.currState}, ,{i},{self.changeState(1)}"
                self.tuCode += f"\n{self.currState},{i},<,{self.currState}"
                self.tuCode += f"\n{self.currState}, ,=,{self.endState()}"
                mov1 = MoveThrought(self.endState(), self.elements, 0 if self.directionTo else 1)
                self.tuCode += mov1.build(alphabet)
                self.uses += 1
                self.tuCode += f"\n{mov1.endState()}, ,{i},{self.changeState(1)}"
                self.tuCode += f"\n{self.currState},{i},>,{temp1}"


        return self.tuCode
