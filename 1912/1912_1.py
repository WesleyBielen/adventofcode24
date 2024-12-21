import os
import time
patterns=list()
calc_patterns=dict()
def main():
    global patterns
    os.chdir(os.path.dirname(__file__))
    file_path = "1912_input_patterns.txt"
    with open(file_path, "r") as file:
        content = file.read()

    patterns = list(x.strip() for x in content.split(','))

    file_path = "1912_input_designs.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    designs = [(line.strip()) for line in content]

    total_found=0
    for design in designs:
        total_found+= shorten(design)

    print(total_found)

def shorten(s):
    global patterns, calc_patterns
    if not s in calc_patterns:
        if len(s)==0:
            return 1
        result = 0
        for pattern in patterns:
            if s.startswith(pattern):
                result+=shorten(s[len(pattern):])
        calc_patterns[s] = result
        return result
    else:
        return calc_patterns[s]

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")