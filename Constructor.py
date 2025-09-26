import os
from string import digits, ascii_uppercase

class Constructor():
    alpha = digits + ascii_uppercase

    def __init__(self, functions: list, power: int):
        self.alpha = self.alpha[:power]
        self.code = "00, ,=,1"
        for x in functions:
            self.code += x.build(self.alpha)

    def build(self, name):
        if os.path.exists(name):
            os.remove("./" + name)
        file = open(name, "w+")
        file.write(self.code)
        file.close 