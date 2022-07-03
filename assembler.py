from Lists import (instructions, opcode, register, Display)
from Type import TypeA


from sys import stdin

halt = False
InstCount = 0

for line in stdin:
    InstCount += 1
    line = line.strip()
    token = [ins for ins in line.split()]

    if halt:
        if instructions[-1] != ["hlt"]:
            raise Exception(
                "Error: halt not being used as the last instruction")
        break

    if ["hlt"] in instructions:
        halt = True

    if token == []:
        continue

    instructions.append(token)


variables = 0
for i in instructions:
    if i[0] == "var":
        variables += 1

InstCode = instructions[variables:]

LineNum = variables

for i in InstCode:
    LineNum += 1
    OpCode = i[0]

    # TypeErrors.TypeA(i,LineNum):
    if(OpCode == "add" or OpCode == "sub" or OpCode == "mul" or OpCode == "xor" or OpCode == "and"):
        Display.append(TypeA(i, LineNum))


for i in Display:
    print(i)
