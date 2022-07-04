from logging import raiseExceptions

from numpy import var
from Lists import (instructions, opcode, register,
                   stored_values, Display, variable, MemAdd, labels)
from Type import TypeA, TypeB, TypeC, TypeD, TypeE, TypeF


from sys import stdin


def split(x):  # Used to split the strings
    return list(x)


halt = False
InstCount = 0

for line in stdin:
    InstCount += 1
    line = line.strip()
    # token contains each instruction as a list
    token = [ins for ins in line.split()]

    if halt:
        if instructions[-1] != ["hlt"]:
            raise Exception(
                "Error: hlt not being used as the last instruction")
        break

    if ["hlt"] in instructions:
        for i in range(len(instructions)):
            label = split(instructions[i][0])
            if ":" in instructions[i] or ":" in label:
                if ":" in label:
                    labelName = (instructions[i][0].split(":"))[0]
                    labels[labelName] = i
                    instructions[i].pop(0)
                else:
                    raise Exception(
                        f"""Error in line {i+1}, A label marks a location in the code and must be followed by a colon (:). No spaces are allowed between label name and colon(:) """
                    )
        halt = True

    if token == []:
        continue

    # print(token)
    instructions.append(token)


variables = 0  # total instrutions containing variables
for i in instructions:
    if i[0] == "var":
        variables += 1


# total instructions to be converted into machine code
InstCode = instructions[variables:]


# raising exception when variables are declared between instructions
for i in InstCode:
    if(InstCode[0] == "var"):
        raise Exception(
            f"""Error in line {variables + i + 1}: Variables should be declared at the beginning of the program""")

LineNum = variables

for i in range(variables):  # Storing the variables in the memory
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

    if(OpCode == "rs" or OpCode == "ls"):
        Display.append(TypeB(i, LineNum))

    if(OpCode == "div" or OpCode == "not" or OpCode == "cmp"):
        Display.append(TypeC(i, LineNum))

    if(OpCode == "ld" or OpCode == "st"):
        Display.append(TypeD(i, LineNum))

    if (OpCode == "jmp" or OpCode == "jlt" or OpCode == "jgt" or OpCode == "je"):
        Display.append(TypeE(i, LineNum))

    if (OpCode == "hlt"):
        Display.append(TypeF(i, LineNum))


for i in Display:
    print(i)
