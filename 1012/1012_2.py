import re
import os
import time

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "1012_input_sample.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    matrix = [list(line.strip()) for line in content]

    for line in matrix:
        print(line)
   
if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")
