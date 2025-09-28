from Function import Function
from MoveThrought import MoveThrought

class CopySymbol(Function):
	def __init__(self, startState, elements, direction: int, rank=4):
		super().__init__(startState, rank)
		self.elements = elements
		self.direction = direction
				
	def code(self, condition: str, action, change=None, startState=None, endState=None):
		return super().code(condition, action, change, startState, endState)
	
	def endState(self, change=None) -> int:
		return super().endState(change)
	
	def changeState(self, rank, change=None) -> str:
		return super().changeState(rank, change)
	
	def startCycle(self, change=None, rank=2):
		return super().startCycle(change, rank)
	
	def build(self, alphabet):
		self.startCycle(1)
		self.code(" ",self.direction,1,self.startState)
		self.code(alphabet,2,0,self.currState,self.startOfCycle)
		for x in alphabet:
			self.code(x," ",1,self.startOfCycle,self.endState())
			mov = MoveThrought(self.endState(),self.elements,self.direction)
			self.tuCode += mov.build(alphabet)
			self.code(" ",self.direction,1,mov.endState())
			self.code(" ",x,1)
			self.code(x,self.direction-1,1,endState=self.endState(2))
			mov1 = MoveThrought(self.endState(),self.elements,self.direction-1)
			self.tuCode += mov.build(alphabet)
			self.endState(1)
			self.code(" ",x,1,startState=mov1.endState(),endState=self.endOfCycle)
		self.code(" "," ",0,self.endOfCycle,self.endState())
		return self.tuCode