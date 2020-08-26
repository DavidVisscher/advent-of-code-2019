"""
Advent of Code day 2

Intcode Computer
"""
import sys
import copy

from typing import List


def load_program(filename = "program.itc") -> List:
    """
    Loads the intcode program from disk.
    """
    rawfile = open(filename, "r")
    programdata = rawfile.read()
    rawfile.close()

    program = [int(instruction.strip()) for instruction in programdata.split(",")]
    return program


def run_program(memory, noun=12, verb=2) -> int:
    """
    Runs the intcode memory and returns the result.
    """

    memory[1] = noun
    memory[2] = verb
    
    instr_pointer = 0

    while True:
        opcode = memory[instr_pointer]
        
        if opcode == 1:
            # Add opcode
            a_addr = memory[instr_pointer+1]
            b_addr = memory[instr_pointer+2]
            q_addr = memory[instr_pointer+3]
            memory[q_addr] = memory[a_addr] + memory[b_addr]
        elif opcode == 2:
            # Multiplication opcode
            a_addr = memory[instr_pointer+1]
            b_addr = memory[instr_pointer+2]
            q_addr = memory[instr_pointer+3]
            memory[q_addr] = memory[a_addr] * memory[b_addr]
        elif opcode == 99:
            break
        instr_pointer += 4

    return memory[0]


def main(target = 19690720):
    """
    Intcode computer main function.
    """
    program = load_program()

    for noun in range(100):
        for verb in range(100):
            print(f"Trying n:{noun} v:{verb}")
            output = run_program(copy.deepcopy(program), noun=noun, verb=verb)
            if output == target:
                print(f"Target values found! Solution: {100 * noun + verb}")
                sys.exit(0)

if __name__ == "__main__":
    main()
