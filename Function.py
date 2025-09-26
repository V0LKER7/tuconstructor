class Function():
    def __init__(self, startState, rank):
        self.startState = startState
        self.idx = 0
        self.uses = 1
        self.rank = rank
        self.states = [0 for i in range(rank)]
        self.states[1] = startState
        self.currState = f"!{"".join(map(str, self.states))}"
        self.tuCode = ''

    def endState(self) -> int:
        return self.states[1] + self.uses
    
    def changeState(self, rank, change=None) -> str:
        if change: 
            self.states[rank] += 1
            self.currState = f"!{"".join(map(str, self.states))}"
        return self.currState
    
    def startCycle(self, change=None, rank=2):
        self.startOfCycle = self.changeState(rank)
        self.endOfCycle = self.changeState(rank, change)
    
    def code(self, condition: str, action: int, change=None, startState=None, endState=None):
        start = startState if startState else self.currState
        end = endState if endState else self.changeState(0,change)
        c=0
        for x in condition:
            c += 1
            self.tuCode += f"\n{start},{x},{"<>=#"[action]},{end}"
        print(c, start)

    def build(self, alphabet: str) -> str:
        self.alphabet = alphabet
        return self.tuCode
