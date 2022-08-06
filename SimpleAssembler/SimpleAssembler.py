# Main file to run the program
from Store import (instructions, opcode, register,
                   stored_values, Display, variable, MemAdd, labels)
from Types import TypeA, TypeB, TypeC, TypeD, TypeE, TypeF
from sys import stdin


def split(x):  # Used to split the strings
    return list(x)


halt = False
InstCount = 0  # to count the lines
for line in stdin:
    InstCount += 1
    line = line.strip()
    # token contains each instruction as a list ['add', 'R1', 'R2', 'R3']
    token = [ins for ins in line.split()]

    if halt:
        for i in range(len(instructions)-1, -1, -1):
            if instructions[i] == []:
                instructions.pop(i)  # To maintain the line number
                continue
        if instructions[-1] != ["hlt"]:
            print(
                "Error: hlt not being used as the last instruction")
        break

    if ["hlt"] in instructions:
        l = 0
        for i in range(len(instructions)):
            l += 1
            if instructions[i] == []:
                l -= 1
                continue
            label = split(instructions[i][0])
            if ":" in instructions[i] or ":" in label:
                if ":" in label:
                    labelName = (instructions[i][0].split(":"))[0]
                    labels[labelName] = i
                    instructions[i].pop(0)
                else:
                    print(
                        f"""Error in line {l}: A label marks a location in the code and must be followed by a colon (:). No spaces are allowed between label name and colon(:) """
                    )
        halt = True

    instructions.append(token)

# if halt == False:
#     print(" Error : hlt is not present")
#     exit()
Variables = 0  # total instructions containing variables
for i in instructions:
    if i == []:
        continue
    if i[0] == "var":
        Variables += 1

# total instructions to be converted into machine code
InstCode = instructions[Variables:]

# raising error when variables are declared between instructions
for i in range(len(InstCode)):
    if(InstCode[0][0] == "var"):
        print(
            f"""Error in line {Variables + i + 1}: Variables should be declared at the beginning of the program""")

LineNum = Variables

for i in range(Variables):  # Storing the variables in the memory
    Var = split(instructions[i])
    MemAdd[Var[1]] = len(InstCode) + i
    variable[Var[1]] = 0


for i in InstCode:
    if i == []:
        continue
    LineNum += 1
    OpCode = i[0]

    # TypeErrors.TypeA(i,LineNum):
    if(OpCode == "add" or OpCode == "sub" or OpCode == "mul" or OpCode == "xor" or OpCode == "and" or OpCode == "or"):
        Display.append(TypeA(i, LineNum))

    elif(OpCode == "mov"):
        X = split(i[-1])
        if "$" in X:
            Display.append(TypeB(i, LineNum))
        else:
            Display.append(TypeC(i, LineNum))

    elif(OpCode == "rs" or OpCode == "ls"):
        Display.append(TypeB(i, LineNum))

    elif(OpCode == "div" or OpCode == "not" or OpCode == "cmp"):
        Display.append(TypeC(i, LineNum))

    elif(OpCode == "ld" or OpCode == "st"):
        if (i[1] not in register.keys()):
            print(f"""Error in line {LineNum} : Invalid Register Provided""")
        if (i[2] not in variable.keys()):
            print(
                f"""Error in line {LineNum} : Variable {i[2]} is not declared""")
        else:
            Display.append(TypeD(i, LineNum))

    elif (OpCode == "jmp" or OpCode == "jlt" or OpCode == "jgt" or OpCode == "je"):
        if i[1] not in labels:
            print(
                f"""Error in line {LineNum} : label {i[1]} is not declared """)
        else:
            Display.append(TypeE(i, LineNum))

    elif (OpCode == "hlt"):
        Display.append(TypeF(i, LineNum))

    if OpCode not in opcode.keys() and OpCode != "mov":
        print("Error : Opcode doesn't exist")
        pass

f = open("output.txt", "w")
for i in Display:
    if i.strip() == "":
        continue
    print(i.strip())
    f.write(i.strip() + "\n")
