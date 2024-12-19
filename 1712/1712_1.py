import os
import time
import re

register_a=0
register_b=0
register_c=0
program=list()
def main():
    global register_a, register_b, register_c, program
    os.chdir(os.path.dirname(__file__))
    file_path = "1712_input.txt"

    with open(file_path, "r") as file:
        content = file.read()

    pattern = r"A:\s*(\d+)"
    match = re.search(pattern, content)
    register_a = match.group(1)

    pattern = r"B:\s*(\d+)"
    match = re.search(pattern, content)
    register_b = match.group(1)

    pattern = r"C:\s*(\d+)"
    match = re.search(pattern, content)
    register_c = match.group(1)


    pattern = r"Program:\s*(.*)"
    match = re.search(pattern, content)
    program = match.group(1).split(",")

    print(register_a)
    print(register_b)
    print(register_c)
    print(program)

    opcode=0
    operand=0
    pointer=0
    output=list()
    while True:
        jumped = False
        opcode=int(program[pointer])
        operand=int(program[pointer+1])

        match opcode:
            case 0:
                register_a = int(int(register_a) / (2 ** get_combo_operand(operand)))
            case 1:
                register_b = int(register_b ^ operand)
            case 2:
                register_b = int(get_combo_operand(operand)) % 8
            case 3:
                if not register_a == 0:
                    pointer=operand
                    jumped=True
            case 4:
                register_b = int(int(register_b) ^ int(register_c))
            case 5:
                output.append(get_combo_operand(operand)%8)
            case 6:
                register_b = int(int(register_a) / (2 ** get_combo_operand(operand)))
            case 7:
                register_c = int(int(register_a) / (2 ** get_combo_operand(operand)))
        if not jumped:
            pointer+=2

        if pointer >= len(program):
            break

    result = ",".join(map(str, output))
    print(result)

def get_combo_operand(operand):
    global register_a, register_b, register_c
    match operand:
        case 1 | 2 | 3:
            return operand
        case 4:
            return register_a
        case 5:
            return register_b
        case 6:
            return register_c
        case 7:
            print("ERROR. Number 7 should not occur in a valid program as a combo operand.")
            exit(1)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")