import os
import string
class Constructor():
    def __init__(self, power):
        self.power = power
        self.alpha = self.alpha[:self.power]
        self.code = f"00, ,<,{self.sysSG(1)}"
        self.numToSim = {a: f"{a}{b}" for a in self.alpha for b in range(self.power)}


    power = 10
    code = ""
    sysState = 0
    state = 0
    numToSim = {}
    alpha = string.digits + string.ascii_uppercase

    def goToLeft1(self):
        for i in range(len(self.alpha)):
            self.code += f"\n{self.sysSG()},{self.alpha[i]},<,{self.sysSG()}"
        self.code += f"\n{self.sysSG()}, ,<,{self.sysSG(1)}"
        for i in range(len(self.alpha)):
            self.code += f"\n{self.sysSG()},{self.alpha[i]},<,{self.sysSG()}"
        self.code += f"\n{self.sysSG()}, ,>,{self.sysSG(1)}"

    def sysSG(self, b = 0):
        self.sysState = self.sysState + b
        return str(self.sysState)
    
    def changeState(self, letter, b):
        if b: self.state = self.state + 1
        return f"!{letter}{self.numToSim[letter]}{self.state}"

    def extractNumber1(self):
        for i in range(len(self.alpha)):
            self.code += f"\n{self.sysSG()},{self.alpha[i]}, ,{3*str(i)}"
            self.code += f"\n{3*str(i)}, ,>,{2*str(i)+"!"}"
        for i in range(len(self.alpha)):
            for x in range(len(self.alpha)):
                self.code += f"\n{2*str(i)+"!"},{self.alpha[x]},>,{2*str(i)+"!"}"
                self.code += f"\n{2*str(i)+"!"}, ,>,{2*str(i)+"@"}"
        for i in range(len(self.alpha)):
            for x in range(len(self.alpha)):
                self.code += f"\n{2*str(i)+"@"},{self.alpha[x]},>,{2*str(i)+"@"}"
                self.code += f"\n{2*str(i)+"@"}, ,>,{2*str(i)+"@"+"&"}"
        for i in range(len(self.alpha)):
            for x in range(len(self.alpha)):
                self.code += f"\n{2*str(i)+"@"+"&"},{self.alpha[x]},>,{2*str(i)+"@"+"&"}"
                self.code += f"\n{2*str(i)+"@"+"&"}, ,=,{2*str(i)+"@"+"@"}"
            self.code += f"\n{2*str(i)+"@"+"@"}, ,{self.alpha[i]},{2*str(i)+"@"+"@"}"
            self.code += f"\n{2*str(i)+"@"+"@"},{self.alpha[i]},<,{2*str(i)+"@"+"-"}"
        for i in range(len(self.alpha)):
            for x in range(len(self.alpha)):
                self.code += f"\n{2*str(i)+"@"+"-"},{self.alpha[x]},<,{2*str(i)+"@"+"-"}"
            self.code += f"\n{2*str(i)+"@"+"-"}, ,<,{2*str(i)+"@"+"+"}"
        for i in range(len(self.alpha)):
            for x in range(len(self.alpha)):
                self.code += f"\n{2*str(i)+"@"+"+"},{self.alpha[x]},<,{2*str(i)+"@"+"+"}"
            self.code += f"\n{2*str(i)+"@"+"+"}, ,<,{2*str(i)+"@"+"%"}"
        for i in range(len(self.alpha)):
            for x in range(len(self.alpha)):
                self.code += f"\n{2*str(i)+"@"+"%"},{self.alpha[x]},<,{2*str(i)+"@"+"%"}"
            self.code += f"\n{2*str(i)+"@"+"%"}, ,{self.alpha[i]},{2*str(i)+"@"+"^"}"
            self.code += f"\n{2*str(i)+"@"+"^"},{self.alpha[i]},>,{self.sysSG()}"
        self.code += f"\n{self.sysSG()}, ,>,{self.sysSG(1)}"

    def goToLeft2(self):
        for i in range(len(self.alpha)):
            self.code += f"\n{self.sysSG()},{self.alpha[i]},<,{self.sysSG()}"
        self.code += f"\n{self.sysSG()}, ,<,{self.sysSG(1)}"
        for i in range(len(self.alpha)):
            self.code += f"\n{self.sysSG()},{self.alpha[i]},<,{self.sysSG(1)}"
        self.code += f"\n{self.sysSG()}, ,>,{self.sysSG(1)}"

    def extractNumber2(self):
        for i in range(len(self.alpha)):
            self.code += f"\n{self.sysSG()},{self.alpha[i]}, ,{4*str(i)}"
            self.code += f"\n{4*str(i)}, ,>,{3*str(i)+"@"}"
        for i in range(len(self.alpha)):
            for x in range(len(self.alpha)):
                self.code += f"\n{3*str(i)+"@"},{self.alpha[x]},>,{3*str(i)+"@"}"
                self.code += f"\n{3*str(i)+"@"}, ,>,{3*str(i)+"-"}"
        for i in range(len(self.alpha)):
            for x in range(len(self.alpha)):
                self.code += f"\n{3*str(i)+"-"},{self.alpha[x]},>,{3*str(i)+"-"}"
                self.code += f"\n{3*str(i)+"-"}, ,>,{3*str(i)+"-"+"*"}"
        for i in range(len(self.alpha)):
            for x in range(len(self.alpha)):
                self.code += f"\n{3*str(i)+"-"+"*"},{self.alpha[x]},>,{3*str(i)+"-"+"*"}"
                self.code += f"\n{3*str(i)+"-"+"*"}, ,=,{3*str(i)+"-"+"-"}"
            self.code += f"\n{3*str(i)+"-"+"-"}, ,{self.alpha[i]},{3*str(i)+"-"+"-"}"
            self.code += f"\n{3*str(i)+"-"+"-"},{self.alpha[i]},<,{3*str(i)+"-"+"+"}"
        for i in range(len(self.alpha)):
            for x in range(len(self.alpha)):
                self.code += f"\n{3*str(i)+"-"+"+"},{self.alpha[x]},<,{3*str(i)+"-"+"+"}"
            self.code += f"\n{3*str(i)+"-"+"+"}, ,<,{3*str(i)+"-"+"%"}"
        for i in range(len(self.alpha)):
            for x in range(len(self.alpha)):
                self.code += f"\n{3*str(i)+"-"+"%"},{self.alpha[x]},<,{3*str(i)+"-"+"%"}"
            self.code += f"\n{3*str(i)+"-"+"%"}, ,<,{3*str(i)+"-"+"^"}"
        for i in range(len(self.alpha)):
            for x in range(len(self.alpha)):
                self.code += f"\n{3*str(i)+"-"+"^"},{self.alpha[x]},<,{3*str(i)+"-"+"^"}"
            self.code += f"\n{3*str(i)+"-"+"^"}, ,{self.alpha[i]},{3*str(i)+"-"+"&"}"
            self.code += f"\n{3*str(i)+"-"+"&"},{self.alpha[i]},>,{self.sysSG()}"
        self.code += f"\n{self.sysSG()}, , ,{self.sysSG(1)}"

    def sum(self):
        self.code += "\n08, ,>,09"
        for x in range(len(self.alpha)):
            self.code += f"\n09,{self.alpha[x]},>,09"
            self.code += f"\n23,{self.alpha[x]},=,24"
            self.code += f"\n24,{self.alpha[x]},>,24"
            self.code += f"\n24, ,◯,24"
            self.code += f"\n24,◯,<,25"
            self.code += f"\n25,{self.alpha[x]},<,25"
            self.code += f"\n25, ,>,30"
        self.code += "\n09, ,<,10"
        for x in range(1, len(self.alpha)):
            self.code += f"\n10,{self.alpha[x]},{self.alpha[x-1]},11"
            self.code += f"\n11,{self.alpha[x-1]},>,11"
            self.code += f"\n15,{self.alpha[x]},{self.alpha[x-1]},16"
        self.code += f"\n10,0,<,15"
        self.code += f"\n15, ,>,23"
        self.code += f"\n23,0, ,23"
        self.code += f"\n23, ,>,23"
        self.code += f"\n15,0,<,15"
        self.code += f"\n11, ,>,12"
        self.code += f"\n17,0,{self.alpha[-1]},17"
        self.code += f"\n17,{self.alpha[-1]},>,17"
        self.code += f"\n17, ,>,12"
        for x in range(len(self.alpha)):
            self.code += f"\n12,{self.alpha[x]},>,12"
            self.code += f"\n16,{self.alpha[x]},>,17"
        self.code += f"\n12, ,<,13"
        for x in range(self.power-1):
            self.code += f"\n13,{self.alpha[x]},{self.alpha[x+1]},14"
            self.code += f"\n18,{self.alpha[x]},{self.alpha[x+1]},19"
            self.code += f"\n19,{self.alpha[x+1]},>,20"
        self.code += f"\n20,{self.alpha[self.power-1]},0,20"
        self.code += f"\n20,0,>,20"
        self.code += f"\n20, ,<,14"
        self.code += f"\n13,{self.alpha[self.power-1]},<,18"
        self.code += f"\n18,{self.alpha[self.power-1]},<,18"
        self.code += f"\n18, ,>,21"
        self.code += f"\n21,{self.alpha[self.power-1]},1,22"
        self.code += f"\n22,1,>,22"
        self.code += f"\n22,{self.alpha[self.power-1]},0,22"
        self.code += f"\n22,0,>,22"
        self.code += f"\n22, ,0,14"
        for x in range(len(self.alpha)):
            self.code += f"\n14,{self.alpha[x]},<,14"
        self.code += f"\n14, ,<,10"

    def answer(self):
        for i in range(len(self.alpha)):
            self.code += f"\n30,{self.alpha[i]}, ,!{2*str(i)}"
            self.code += f"\n!{2*str(i)}, ,<,!{2*str(i)+"!"}"
            for x in range(len(self.alpha)):
                self.code += f"\n!{2*str(i)+"!"},{self.alpha[x]},>,!{2*str(i)+"@"}"
                self.code += f"\n!{2*str(i)+"&"},{self.alpha[x]},=,31"
                self.code += f"\n!{2*str(i)+"b"},{self.alpha[x]},>,!{2*str(i)+"+"}"
                self.code += f"\n32,{self.alpha[x]},>,33"
            
            self.code += f"\n!{2*str(i)+"!"}, ,<,!{2*str(i)+"!"}"
            self.code += f"\n!{2*str(i)+"@"}, ,>,!{2*str(i)+"$"}"
            self.code += f"\n!{2*str(i)+"$"}, ,{self.alpha[i]},!{2*str(i)+"%"}"
            self.code += f"\n!{2*str(i)+"%"},{self.alpha[i]},>,!{2*str(i)+"^"}"
            self.code += f"\n!{2*str(i)+"^"}, ,>,!{2*str(i)+"&"}"
            self.code += f"\n31,{self.alpha[i]}, ,!{2*str(i)+"*"}"
            self.code += f"\n!{2*str(i)+"*"}, ,<,!{2*str(i)+"m"}"
            self.code += f"\n!{2*str(i)+"&"}, ,>,!{2*str(i)+"&"}"
            self.code += f"\n!{2*str(i)+"m"}, ,<,!{2*str(i)+"b"}"
            self.code += f"\n!{2*str(i)+"+"}, ,{self.alpha[i]},!{2*str(i)+"%"}"
            self.code += f"\n!{2*str(i)+"b"}, ,<,!{2*str(i)+"b"}"
            self.code += f"\n!{2*str(i)+"&"},◯, ,32"
            self.code += f"\n32, ,<,32"
            self.code += f"\n33, , ,33"


    def build(self, name: str):
        self.goToLeft1()
        self.extractNumber1()
        # self.goToLeft2()
        self.extractNumber2()
        self.sum()
        self.answer()
        if os.path.exists(name):
            os.remove("./" + name)
        file = open(name, "w+")
        file.write(self.code)
        file.close

if __name__ == "__main__":
    constructor = Constructor(2)
    constructor.build("sum.tu4")