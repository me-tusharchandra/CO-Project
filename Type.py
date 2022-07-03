from Lists import (instructions, opcode, register,
                   stored_values, Display, variable, MemAdd, Flag)


def add_Binary(a, b):
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


def bintodec(bin_str):
    bin_num = str(bin_str)
    # print(bin_num)
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
    if(len(inst) != 4):
        raise Exception(
            f"""TypoError in line{line} : Type A -> 3 Register type""")
    code += opcode[inst[0]]  # opcode
    code += "00"  # unused bits
    code += register[inst[1]]
    code += register[inst[2]]
    code += register[inst[3]]
    Result = 0
    if len(inst) > 3:
        if(inst[0] == "add"):

            reg1 = stored_values[inst[1]]
            reg2 = stored_values[inst[2]]
            Result = add_Binary(str(reg1), str(reg2))
            if(len(str(Result)) > 8):
                Flag[0] = True
                stored_values[inst[3]] = 0
                raise Exception(f"""Error: Overflow!""")
            else:
                stored_values[inst[3]] = Result

        if(inst[0] == "sub"):
            reg1 = stored_values[inst[1]]
            reg2 = stored_values[inst[2]]
            operand1 = bintodec(str(reg1))
            operand2 = bintodec(str(reg2))
            if(operand1 < operand2):
                Flag[0] = True
                raise Exception("""Error : Overflow!""")
            else:
                sub = operand1 - operand2
                result = sub
            result = f'{sub:08}'
            stored_values[inst[3]] = Result

        if(inst[0] == "mul"):
            reg1 = stored_values[inst[1]]
            reg2 = stored_values[inst[2]]
            operand1 = bintodec(str(reg1))
            operand2 = bintodec(str(reg2))

            mul = operand1 * operand2
            result = mul
            result = f'{mul:08}'
            stored_values[inst[3]] = Result

    return code


def TypeB(inst,  line):
    code = ""
    if(len(inst) != 3):
        raise Exception(
            f"""TypoError in line {line} : Type B -> 1 register and Immediate type"""
        )
    if(len(inst) > 2):
        if inst[0] == "mov":
            code += "10001"
            code += register[inst[1]]
            imm = int(inst[-1].split("$")[-1])
            if (imm > 255) or (imm < 0):
                raise Exception(
                    f"""Error in line {line} : A Imm must be a whole number <= 255 and >= 0"""
                )
            # print(stored_values[inst[1]])
            Binary = f"{imm:08b}"
            stored_values[inst[1]] = Binary
            # print(stored_values[inst[1]])
            code += Binary

    return code


def TypeC(inst, line):
    code = ""
    if(len(inst) != 3):
        raise Exception(
            f"""TypoError in line {line} : Type C -> 2 registers type"""
        )
    if (inst[0] == "mov"):
        code += "10011"
        code += register[inst[1]]
        code += register[inst[2]]
        stored_values[inst[1]] = register[inst[1]]
        stored_values[inst[2]] = register[inst[2]]
        register[inst[2]] = register[inst[1]]
        stored_values[inst[2]] = stored_values[inst[1]]
    return code


def TypeD(inst, line):
    code = ""
    code += opcode[inst[0]]
    if(len(inst) != 3):
        raise Exception(
            f"""TypoError in line {line} : Type D -> 1 register type and memory address type"""
        )
    if(inst[0] == "ld"):
        stored_values[inst[1]] = variable[inst[2]]

    if(inst[0] == "st"):
        variable[inst[2]] = stored_values[inst[1]]

    code += register[inst[1]]
    var = f'{MemAdd[inst[2]]:08b}'
    code += var
    return code


def TypeE(inst, line):
    pass
