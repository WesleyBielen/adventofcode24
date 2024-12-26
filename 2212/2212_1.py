import os
import time

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "2212_input.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    buyers = [int(line.strip()) for line in content]

    total_secrets=0
    for buyer in buyers:
        number = buyer
        for i in range(2000):
            step1 = number * 64
            step2 = number ^ step1
            step3 = step2 % 16777216
            step4 = int(step3 / 32)
            step5 = step3 ^ step4
            step6 = step5 % 16777216
            step7 = step6 * 2**11
            step8 = step6 ^ step7
            number = step8 % 16777216
        total_secrets+=number

    print(total_secrets)
if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")