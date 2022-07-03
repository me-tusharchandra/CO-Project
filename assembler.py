from Lists import (instructions, opcode, register,
                   stored_values, Display, variable, MemAdd)
from Type import TypeA, TypeB, TypeC, TypeD, TypeE


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
                "Error: hlt not being used as the last instruction")
        break

    if ["hlt"] in instructions:
        halt = True

    if token == []:
        continue

    instructions.append(token)


def split(x):
    return list(x)


variables = 0
for i in instructions:
    if i[0] == "var":
        variables += 1


InstCode = instructions[variables:]

LineNum = variables


for i in range(variables):
    Var = split(instructions[i])

    MemAdd[Var[1]] = len(InstCode) + i
    variable[Var[1]] = 0


for i in InstCode:
    LineNum += 1
    OpCode = i[0]

    # TypeErrors.TypeA(i,LineNum):
    if(OpCode == "add" or OpCode == "sub" or OpCode == "mul" or OpCode == "xor" or OpCode == "and"):
        Display.append(TypeA(i, LineNum))

    if(OpCode == "mov"):
        X = split(i[-1])
        if "$" in X:
            Display.append(TypeB(i, LineNum))
        else:
            Display.append(TypeC(i, LineNum))

    if(OpCode == "ld" or OpCode == "st"):
        Display.append(TypeD(i, LineNum))


for i in Display:
    print(i)
