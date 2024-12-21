
file = open(__file__ + '\\..\\testInput.txt', 'r')
#file = open(__file__ + '\\..\\input.txt', 'r')
program = []
class Ins:

    output = ''
    regA = 0
    regB = 0
    regC = 0
    program = []
    pointer = 0

    def __init__(self, regA, regB, regC, program):
        self.regA = regA
        self.regB = regB
        self.regC = regC
        self.program = program

    def __str__(self) -> str:
        return f"regA: {self.regA} regB: {self.regB} regC: {self.regC}"

    def printOutput(self):
        print(self.output)

    def processProgram(self):
        while self.pointer + 1 < len(program):
            ins.doInstruction(program[self.pointer], program[self.pointer+1])
            self.pointer += 2

    def doInstruction(self, instNo, operand):
        comboVal = operand
        if operand <= 3:
            comboVal = operand
        elif operand == 4:
            comboVal = self.regA
        elif operand == 5:
            comboVal = self.regB
        elif operand == 6:
            comboVal = self.regC


        if instNo == 0:
            val = int(self.regA / pow(2, comboVal))
            self.regA = val
        elif instNo == 1:        
            self.regB = self.regB ^ operand
        elif instNo == 2: #(thereby keeping only its lowest 3 bits) ????
            self.regB = comboVal % 8
        elif instNo == 3:
            if self.regA == 0:
                return
            self.pointer = operand - 2
        elif instNo == 4:
            self.regB = self.regB ^ self.regC
        elif instNo == 5:
            out = list(str(comboVal % 8))
            if self.output != '':
                self.output += ','
            self.output += ','.join(out)
        elif instNo == 6:
            val = int(self.regA / pow(2, comboVal))
            self.regB = val
        elif instNo == 7:
            val = int(self.regA / pow(2, comboVal))
            self.regC = val


regA = 0
regB = 0
regC = 0
for i, line in enumerate(file.readlines()):
    line = line.removesuffix('\n')
    vals = line.split(': ')
    if "Register A" == vals[0]:
        regA = int(vals[1])
    if "Register B" == vals[0]:
        regB = int(vals[1])
    if "Register C" == vals[0]:
        regC = int(vals[1])

    if "Program" == vals[0]:
        program = list(map(int, (vals[1].split(','))))

ins = Ins(regA, regB, regC, program)

ins.processProgram()
print(ins.printOutput())
print(ins)