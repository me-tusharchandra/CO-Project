from Store import (instructions, opcode, register,
                   stored_values, Display, variable, MemAdd, Flag, labels)

import struct


def binary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))

def add_Binary(a, b):  # function to add two binary numbers
    maxlen = max(len(a), len(b))

    a = a.zfill(maxlen)
    b = b.zfill(maxlen)

    result = ""

    carry = 0

    for i in range(maxlen - 1, -1, -1):
        x = carry
        x += 1 if a[i] == "1" else 0
        x += 1 if b[i] == "1" else 0
        result = ("1" if x % 2 == 1 else "0") + result
        carry = 0 if x < 2 else 1

    if carry != 0:
        result = '1' + result

    return result.zfill(maxlen)


def bintodec(bin_str):  # function to convert binary into decimal
    bin_num = str(bin_str)
    dec = 0
    n = len(bin_num)
    for i in range(n):
        if bin_num[n - i - 1] == "1":
            dec += pow(2, i)
        else:
            continue
    return dec


def TypeA(inst, line):
    code = ""
        
    code += opcode[inst[0]]  # opcode
    code += "00"  # unused bits
    if(inst[1] not in register.keys() or inst[2] not in register.keys() or inst[3] not in register.keys()):
        return print(f"""Error in line {line} : Invalid register provided""")
    code += register[inst[1]]
    code += register[inst[2]]
    code += register[inst[3]]
    Result = 0
    reg1 = stored_values[inst[1]]
    reg2 = stored_values[inst[2]]
    operand1 = bintodec(str(reg1))
    operand2 = bintodec(str(reg2))
    # if len(inst) > 3:
        # if(inst[0] == "add"):

        #     reg1 = stored_values[inst[1]]
        #     reg2 = stored_values[inst[2]]
        #     Result = add_Binary(str(reg1), str(reg2))
        #     # if(len(str(Result)) > 8):
        #     #     Flag[0] = True
        #     #     stored_values[inst[3]] = 0
        #     #     print(f"""Error: Overflow!""")
        #     # else:
        #     #     stored_values[inst[3]] = Result

        # if(inst[0] == "sub"):
        #     # if(operand1 < operand2):
        #     #     Flag[0] = True
        #     #     print("""Error : Overflow!""")
        #     # else:
        #     #     sub = operand1 - operand2
        #     # result = f'{sub:08b}'
        #     # stored_values[inst[3]] = result

        # if(inst[0] == "mul"):
        #     # mul = operand1 * operand2
        #     # result = mul
        #     # result = f'{mul:08b}'
        #     # stored_values[inst[3]] = Result

        # if(inst[0] == "xor"):
        #     # xor = operand1 ^ operand2
        #     # result = xor
        #     # result = f'{xor:08b}'
        #     # stored_values[inst[3]] = Result

        # if(inst[0] == "or"):
        #     Or = operand1 | operand2
        #     result = Or
        #     result = f'{Or:08b}'
        #     stored_values[inst[3]] = Result

        # if(inst[0] == "and"):
        #     And = operand1 & operand2
        #     result = And
        #     result = f'{And:08b}'
        #     stored_values[inst[3]] = Result
    return code


def TypeB(inst,  line):
    code = ""
    if(len(inst) != 3):
        print(
            f"""TypoError in line {line} : Type B -> 1 register and Immediate type"""
        )
    if(len(inst) > 2):
            imm = int(inst[-1].split("$")[-1])
            if (imm > 255) or (imm < 0):
                print(
                    f"""Error in line {line} : A Imm must be a whole number <= 255 and >= 0"""
                )
            if inst[0] == "mov":
                code += "10010"
                code += register[inst[1]]
                Binary = f"{imm:08b}"
                stored_values[inst[1]] = Binary
                code += Binary

            if inst[0] == "ls":
                code += opcode[inst[0]]
                code += register[inst[1]]
                ls = register[inst[1]]
                stored_values[inst[1]] = ls
                Binary = f"{imm:08b}"
                stored_values[inst[1]] = Binary
                code += Binary
                

            if inst[0] == "rs":
                code += opcode[inst[0]]
                code += register[inst[1]]
                rs = register[inst[1]]
                stored_values[inst[1]] = rs
                Binary = f"{imm:08b}"
                stored_values[inst[1]] = Binary
                code += Binary
    return code


def TypeC(inst, line):
    code = ""
    if(len(inst) != 3):
        print(
            f"""TypoError in line {line} : Type C -> 2 registers type"""
        )
    if(inst[1] not in register.keys() or inst[2] not in register.keys()):
        if inst[1] != "FLAGS" or inst[0] != "mov" or inst[2] not in register.keys():
            print(
                f"""Error in line {line} : Invalid register provided""")
    if (inst[0] == "mov"):
        code += "10011"
        stored_values[inst[1]] = register[inst[1]]
        stored_values[inst[2]] = register[inst[2]]

    if(inst[0] == "div"):
        code += opcode[inst[0]]
    #     reg1 = stored_values[inst[1]]
    #     reg2 = stored_values[inst[2]]
    #     operand1 = bintodec(str(reg1))
    #     operand2 = bintodec(str(reg2))

    #     div = operand1/operand2
    #     stored_values["R0"] = operand1 // operand2
    #     stored_values["R1"] = operand1 % operand2

    if(inst[0] == "not"):
        code += opcode[inst[0]]
        # reg1 = stored_values[inst[1]]
        # reg2 = stored_values[inst[2]]
        # operand1 = bintodec(str(reg1))
        # operand2 = bintodec(str(reg2))
        # reg = stored_values[inst[2]]

        # Not = ""
        # for i in range(len(reg)):
        #     if Not[i] == "1":
        #         Not = Not + "0"
        #     else:
        #         Not = Not + "1"

        # stored_values[inst[1]] = Not

    if(inst[0] == "cmp"):
        code += opcode[inst[0]]
        # reg1 = stored_values[inst[1]]
        # reg2 = stored_values[inst[2]]
        # operand1 = bintodec(str(reg1))
        # operand2 = bintodec(str(reg2))
        # if(operand1 > operand2):
        #     Flag[-2] = True
        # elif(operand2 > operand1):
        #     Flag[-3] = True
        # else:
        #     Flag[-1] = True

    code += "00000"
    code += register[inst[1]]
    code += register[inst[2]]
    return code


def TypeD(inst, line):
    code = ""
    if(len(inst) != 3):
        print(
            f"""TypoError in line {line} : Type D -> 1 register type and memory address type"""
        )
    if(inst[0] == "ld"):
        stored_values[inst[1]] = variable[inst[2]]

    if(inst[0] == "st"):
        variable[inst[2]] = stored_values[inst[1]]

    code += opcode[inst[0]]
    code += register[inst[1]]
    var = f'{MemAdd[inst[2]]:08b}'
    code += var
    return code


def TypeE(inst, line):
    code = ""
    code += opcode[inst[0]]
    code += "000"

    if inst[0] == "jmp":
        lineToJump = labels[inst[1]]
    if inst[0] == "jlt":
        lineToJump = labels[inst[1]]
    if inst[0] == "jgt":
        lineToJump = labels[inst[1]]
    if inst[0] == "je":
        lineToJump = labels[inst[1]]

    mem = labels[inst[1]]
    result = f'{mem:08b}'
    code += result
    return code


def TypeF(inst, line):
    code = ""
    code += opcode[inst[0]]
    code += "0" * 11
    return code


def TypeF_Addition(inst, line):
    code = ""
    code += "00000"  # opcode
    code += "00"
    code += register[inst[1]]
    code += register[inst[2]]
    code += register[inst[3]]
    return code


def TypeF_Subtraction(inst, line):
    code = ""
    code += "00001"  # opcode
    code += "00"
    code += register[inst[1]]
    code += register[inst[2]]
    code += register[inst[3]]
    return code


def TypeMoveF_Immediate(inst, line):
    code = ""
    imm = float(inst[-1].split("$")[-1])
    Binary = binary(imm)
    code += "00010"
    code += register[inst[1]]
    code += Binary
    code = code[0:16]
    return code


