from sys import stdin


def convertToBin(num, bits):
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

def convertToDec(binary):
    binary = str(binary)
    n = len(binary)
    ans = 0
    for i in range(n):
        if binary[n - i - 1] == "1":
            ans += pow(2, i)
        else:
            continue
    return ans
    

def decimalToBinary(n):
    return int(bin(n).replace("0b", ""))

def TypeA(i):
    opcode = i[0:5]
    destination_register = i[7:10]
    reg1 = i[10:13]
    reg2 = i[13:]
    opcode1 = storedregister[reg1]
    opcode2 = storedregister[reg2]

    if(opcodes[opcode] == "add"):
        



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
pc = 0 #program counter
memory = [] #memory
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

x_axis = []
y_axis = []


for line in stdin:

    line = line.strip()
    if line == "":
        continue

#temp
    if line == "s":
        memory.append(1001100000000000)
        break
    memory.append(line)
#temp

while(len(memory) < 265):
    memory.append(convertToBin(0,16))

cycle = 0

end = False
while(pc < len(memory)):

    if end:
        break

    x_axis.append(cycle)
    y_axis.append(pc)
    cycle += 1

    pcBIN = convertToBin(pc,8)

    ReadingFlag = storedregister["111"]

    storedregister["111"] = 0

    opcode = memory[pc][0:5]

    if(opcodes[opcode] == "hlt"):
        end = True
    
    if(
        (opcodes[opcode] == "add") or
        (opcodes[opcode] == "sub") or
        (opcodes[opcode] == "mul") or
        (opcodes[opcode] == "xor") or
        (opcodes[opcode] == "or")  or
        (opcodes[opcode] == "and")
    ):
    # typeA
