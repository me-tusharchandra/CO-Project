opcode = {
    "add": "10000",
    "sub": "10001",
    "ld": "10100",
    "st": "10101",
    "mul": "10110",
    "div": "10111",
    "rs": "11000",
    "ls": "11001",
    "xor": "11010",
    "or": "11011",
    "and": "111000",
    "not": "11101",
    "cmp": "11110",
    "jmp": "11111",
    "jlt": "01100",
    "jgt": "01101",
    "je": "01111",
    "hlt": "01010"
}

register = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    # "FLAGS": "111",
}

stored_values = {
    "R0":  0,
    "R1":  0,
    "R2":  0,
    "R3":  0,
    "R4":  0,
    "R5":  0,
    "R6":  0,
    "FLAGS": "0"*16,
    "PC": 0
}

instructions = []

variable = {}

MemAdd = {}

labels = {}

Display = []

Flag = [False, False, False, False]
