import os
import time

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "2112_input.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    buyers = [int(line.strip()) for line in content]

    all_sequencev = dict()
    for buyer in buyers:
        number = buyer
        prev_digit = None
        sequence=list()
        buyer_sequencev = dict()
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
            digit = number % 10

            if i == 0:
                number = buyer
                digit = number % 10

            if i > 0:
                diff = digit - prev_digit
                sequence.append(diff)

            if len(sequence) == 4:
                if not tuple(sequence) in buyer_sequencev:
                    buyer_sequencev[tuple(sequence)] = digit
                sequence.pop(0)

            prev_digit = digit

        for k,v in buyer_sequencev.items():
            if k in all_sequencev:
                all_sequencev[k] += v
            else:
                all_sequencev[k] = v

    max_key = max(all_sequencev, key=all_sequencev.get)
    max_value = all_sequencev[max_key]
    print(f'Max key = {max_key} . Max val = {max_value}')

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")