opcode = {"add": "00000", 
          "sub": "00001",
          "ld": "00100",
          "st": "00101",
          "mul": "00110",
          "div": "00111",
          "rs": "01000",
          "ls": "01001",
          "xor": "01010",
          "or": "01011",
          "and": "01100",
          "not": "01101",
          "cmp": "01110",
          "jmp": "01111",
          "jlt": "10000",
          "jgt": "10001",
          "je": "10010",
          "hlt": "10011"
          }

register = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "FLAGS": "111",
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
