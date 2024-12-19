import os
import time

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "1812_input_sample.txt"

    with open(file_path, "r") as file:
        content = file.read()


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")