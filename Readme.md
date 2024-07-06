# **Assember - Simulator**



# A. Assembler for Custom Instruction Set Architecture

This Python program serves as an assembler for a custom Instruction Set Architecture (ISA). It reads a series of assembly-like instructions from the standard input and converts them into machine code suitable for the custom ISA. The program performs the following key tasks:

## Functionality:

1. **Instruction Parsing**: It parses the input instructions, tokenizes them, and prepares them for further processing.

2. **Label Handling**: The program manages labels and their associated memory addresses, which are important for branching and memory operations.

3. **Instruction Validation**: It identifies and validates different instruction types based on the custom ISA's format. These include TypeA, TypeB, TypeC, TypeD, TypeE, TypeF, TypeF_Addition, TypeF_Subtraction, and TypeMoveF_Immediate.

4. **Error Handling**: The program checks for errors, such as incorrect instruction formats and the absence of an 'hlt' instruction as the last instruction in the program.

5. **Machine Code Generation**: It outputs the converted machine code for each instruction, which can be used to execute programs on the custom ISA.

## Usage:

To use this assembler, provide a text file containing the assembly-like instructions as input to the program. Ensure that the input adheres to the specific instruction set of the custom architecture.

# B. Custom ISA Simulator

This Python program simulates the execution of programs written in a custom Instruction Set Architecture (ISA). The simulator performs the following key functions:

## Functionality:

1. **Instruction Parsing**: Reads and interprets assembly-like instructions from the standard input.

2. **Instruction Execution**: Executes instructions, including arithmetic operations, memory access, shifts, comparisons, and control flow instructions.

3. **Memory Simulation**: Maintains and simulates memory for storing values and instructions.

4. **Flag Handling**: Manages flags to track conditions such as comparisons.

5. **Cycle and Register Monitoring**: Keeps track of execution cycles and the values of registers during execution.

6. **Graphical Output**: Generates a graphical representation of memory access patterns during execution.

## Usage:

To use the simulator, provide a program written in the custom ISA's assembly-like language as input to the program via standard input. The program will execute the instructions and provide cycle-by-cycle details of the execution.





