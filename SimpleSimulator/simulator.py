#importing library for taking stdin
from sys import stdin

#Function to convert Decimal to binary


def DecToBinary(num, bits):
    if num == 0:
        return '0' * bits
    result = ""
    while num > 1:
        result = str(num % 2) + result
        num = num // 2
    result = "1" + result
    bitsLeft = bits - len(result)
    if bitsLeft > 0:
        result = '0' * bitsLeft + result
    return result

#function to convert Binary to decimal


def BinaryToDec(binary):
    binary = str(binary)
    lenght = len(binary)
    result = 0
    for i in range(lenght):
        if binary[lenght - i - 1] == "1":
            result += pow(2, i)
        else:
            continue
    return result

#To print the values of program counter and Registers


def Print_pcAndreg(Pcount):
    print(Pcount, end=" ")
    for i in storedregister.values():
        Registervalue = DecToBinary(i, 16)
        print(Registervalue, end=" ")
    print()

#Function to print memory values


def Print_Memory(m):
    for i in range(len(m)):
        print(m[i])

#Type of functions


def TypeA(inst):
    opcode = inst[0:5]
    Final = inst[7:10]
    reg1 = inst[10:13]
    reg2 = inst[13:]
    operand1 = storedregister[reg1]
    operand2 = storedregister[reg2]

#for add instruction
    if(opcodes[opcode] == "add"):
        Result = operand1 + operand2
        BinResult = DecToBinary(Result, 16)
    #overflow case
        if len(BinResult) > 16:
            BinResult = BinResult[-16:]
            storedregister["111"] = 8
            Result = BinaryToDec(BinResult)

#for sub instruction
    elif(opcodes[opcode] == "sub"):
        Result = operand1 - operand2
        #if the value is negative
        if (Result < 0):
            Result = 0
            storedregister["111"] = 8

#for multiply instruction
    elif(opcodes[opcode] == "mul"):
        Result = operand1 * operand2
        resInBin = DecToBinary(Result, 16)
        #Overflow case
        if len(resInBin) > 16:
            resInBin = resInBin[-16:]
            storedregister["111"] = 8
            Result = BinaryToDec(resInBin)

#for xor instruction
    elif(opcodes[opcode] == "xor"):
        Result = operand1 ^ operand2

#for or instrution
    elif(opcodes[opcode] == "or"):
        Result = operand1 | operand2

#for and instruction
    elif(opcodes[opcode] == "and"):
        Result = operand1 & operand2

#storing result in destination register
    storedregister[Final] = Result


#for type B instructions
def TypeB(inst):
    opcode = inst[0:5]
    reg = inst[5:8]

    #to convert imm value to binary
    imm = BinaryToDec(inst[8:])
    valuesShiftTo = DecToBinary(storedregister[reg], 16)
    valuesShiftBy = "0"*imm

#instruction for mov
    if (opcodes[opcode] == "mov"):

        #storing value of imm into the reg
        storedregister[reg] = imm

#instruction for left shift
    elif (opcodes[opcode] == "ls"):
        result = valuesShiftTo + valuesShiftBy
        result = result[-16:]
        storedregister[reg] = BinaryToDec(result)

#instruction for right shift
    elif (opcodes[opcode] == "rs"):
        result = valuesShiftBy + valuesShiftTo
        result = result[0:16]
        storedregister[reg] = BinaryToDec(result)

#instruction for type C
def TypeC(inst, CurrentFlag):
    opcode = inst[0:5]
    reg1 = inst[10:13]
    reg2 = inst[13:]

#inst for cmp
    if (opcodes[opcode] == "cmp"):
        CmpValue1 = storedregister[reg1]
        CmpValue2 = storedregister[reg2]
        if (CmpValue1 >= CmpValue2):
            storedregister["111"] = 2
        elif (CmpValue1 <= CmpValue2):
            storedregister["111"] = 4
        else:
            storedregister["111"] = 1

#for not inst
    elif (opcodes[opcode] == "not"):
        num = DecToBinary(storedregister[reg2], 16)

        Result = ""
        for i in range(len(num)):
            if(num[i] == "1"):
                Result = Result + "0"
            else:
                Result = Result + "1"
        inverted = BinaryToDec(Result)
        storedregister[reg1] = inverted

#for div instruction
    elif (opcodes[opcode] == "div"):
        quotient = (storedregister[reg1]) // (storedregister[reg2])
        remainder = storedregister[reg1] % storedregister[reg2]
        storedregister["000"] = quotient
        storedregister["001"] = remainder

#for mov inst
    elif (opcodes[opcode] == "mov"):
        if(reg2 == "111"):
            storedregister[reg1] = CurrentFlag
            return
        storedregister[reg1] = storedregister[reg2]


#for type D instruction
def TypeD(inst):
    opcode = inst[0:5]
    reg = inst[5:8]
    address = BinaryToDec(inst[8:])
    storedValue = storedregister[reg]
    LoadValue = BinaryToDec(memory[address])

#for st inst
    if(opcodes[opcode] == "st"):
        memory[address] = DecToBinary(storedValue, 16)

#for ld inst
    elif(opcodes[opcode] == "ld"):
        storedregister[reg] = LoadValue

#for type E inst
def TypeE(inst, Pcount, CurrentFlag):
    opcode = inst[0:5]
    address = BinaryToDec(inst[8:])

#for jmp inst
    if(opcodes[opcode] == "jmp"):
        Pcount = address

#for jgt inst
    elif (opcodes[opcode] == "jgt"):
        if(CurrentFlag == 2):
            Pcount = address
        else:
            Pcount += 1

#for jlt inst
    elif (opcodes[opcode] == "jlt"):
        if(CurrentFlag == 4):
            Pcount = address
        else:
            Pcount += 1

#for je isnt
    elif (opcodes[opcode] == "je"):
        if(CurrentFlag == 1):
            Pcount = address
        else:
            Pcount += 1

    return Pcount


#op codes for instructions
opcodes = {
    "00000": "add",
    "00001": "sub",
    "00100": "ld",
    "00101": "st",
    "00110": "mul",
    "00111": "div",
    "01000": "rs",
    "01001": "ls",
    "01010": "xor",
    "01011": "or",
    "01100": "and",
    "01101": "not",
    "01110": "cmp",
    "01111": "jmp",
    "10000": "jlt",
    "10001": "jgt",
    "10010": "je",
    "10011": "hlt"
}


storedregister = {
    "000": 0,
    "001": 0,
    "010": 0,
    "011": 0,
    "100": 0,
    "101": 0,
    "110": 0,
    "111": 0,
}

# x_axis = []
# y_axis = []

memory = []  # memory
#Taking stdin input
for line in stdin:

    #for Removing spaces between instruction
    line = line.strip()

    #for handeling blank lines
    if line == "":
        continue

# #temp
    if line == "s":
        memory.append(1001100000000000)
        break
# #temp

#adding all instruction in the memory as list of instructions
    memory.append(line)


# while(len(memory) < 265):
#     memory.append(DecToBinary(0, 16))

cycle = 0  # cycle
pc = 0  # program counter
hlt = False
while(pc < len(memory)):

    #looping over the instruction untill it encounters hlt
    if hlt:
        break

    # x_axis.append(cycle)
    # y_axis.append(pc)
    # cycle += 1

    pcBIN = DecToBinary(pc, 8)

    ReadingFlag = storedregister["111"]

    storedregister["111"] = 0

    opcode = memory[pc][0:5]

    if(opcodes[opcode] == "hlt"):
        hlt = True

    if(
        (opcodes[opcode] == "add") or
        (opcodes[opcode] == "sub") or
        (opcodes[opcode] == "mul") or
        (opcodes[opcode] == "xor") or
        (opcodes[opcode] == "or") or
        (opcodes[opcode] == "and")
    ):
        TypeA(memory[pc])

    elif(opcodes[opcode] == "mov"):
        if(memory[pc][13:]) in storedregister:
            TypeC(memory[pc], ReadingFlag)
        else:
            TypeB(memory[pc])

    elif (
        (opcodes[opcode] == "cmp") or
        (opcodes[opcode] == "div") or
        (opcodes[opcode] == "not")
    ):
        TypeC(memory[pc], ReadingFlag)

    elif(
        (opcodes[opcode] == "ls") or
        (opcodes[opcode] == "rs")
    ):
        TypeB(memory[pc])

    elif(
            (opcodes[opcode] == "ld") or
            (opcodes[opcode] == "st")):
        # cycle -= 1
        # x_axis.append(cycle)
        # y_axis.append(BinaryToDec(memory[pc][-8:]))
        # cycle += 1
        TypeD(memory[pc])

    elif(
            (opcodes[opcode] == "jmp") or
            (opcodes[opcode] == "jgt") or
            (opcodes[opcode] == "jlt") or
            (opcodes[opcode] == "je")):
        pc = TypeE(memory[pc], pc, ReadingFlag,)
        Print_pcAndreg(pcBIN)
        continue

    Print_pcAndreg(pcBIN)
    print(memory)

    pc += 1
Print_Memory(memory)

