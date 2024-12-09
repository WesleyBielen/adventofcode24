import os
import time

operator_mapping = {
    '0': lambda x, y: x + y,
    '1': lambda x, y: x * y
}
def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "712_input.txt"

    list1 = []
    list2 = []

    with open(file_path, "r") as file:
        for line in file:
            part1, part2 = line.split(": ")
            list1.append(int(part1))
            list2.append([int(x) for x in part2.split()])

    total_sum  = 0
    for i in range(len(list2)):
        outcome = list1[i]
        numbers_length = len(list2[i])
        equation_found=False
        for ii in range(2**(numbers_length-1)):
            binary_format = get_binary_format(ii, numbers_length-1)
            equation=0
            for iii in range(len(binary_format)):
                if equation == 0:
                    equation=operator_mapping[binary_format[iii]](list2[i][iii],list2[i][iii+1])
                else:
                    equation=operator_mapping[binary_format[iii]](equation,list2[i][iii+1])
            if equation == outcome:
                equation_found=True
                break
        if equation_found:
            total_sum+=outcome

    print(total_sum)

def get_binary_format(num, length):
    binary_format_no_prefix = bin(num)[2:]
    return binary_format_no_prefix.zfill(length)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")
