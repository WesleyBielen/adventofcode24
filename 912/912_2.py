import re
import os
import time

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "912_input.txt"

    with open(file_path, "r") as file:
        content = file.read()

    new_string = ""
    alt = False
    file_block_num=0
    for i in range(len(content)):
        if alt:
            new_string+=  str('.' * int(content[i]))
        else:
            new_string += str(str('-'+str(file_block_num)+'-') * int(content[i]))
            file_block_num+=1
        alt = not alt
    for i in range(file_block_num, 0, -1):
        num_times_file_block_id_is_printed = int((content[(i*2)-2]))
        new_string = swap(i-1, num_times_file_block_id_is_printed, new_string)
        if not (re.search(r"(?<=-)\.(?=-)", new_string)):
            break

    print(new_string)
    total_sum = 0
    pattern = r"-(\d+)-"
    matches = re.findall(pattern, new_string)
    numbers = list(map(int, matches))

    for i in range(len(numbers)):
        amount_of_free_blocks = get_amount_of_free_blocks_before_num(new_string, numbers[i])
        total_sum+= numbers[i] * (i+amount_of_free_blocks)

    print(total_sum)

def get_amount_of_free_blocks_before_num(new_string, number):
    index_file_block_id = new_string.find(('-'+str(number)+'-'))
    return new_string[:index_file_block_id].count('.')

def swap(file_block_id, num_times_file_block_id_is_printed, new_string):
    index_file_block_id = new_string.rfind(('-'+str(file_block_id)+'-') * num_times_file_block_id_is_printed)
    if not (re.search(r"(?<=-)\.(?=-)", new_string)):
        return
    length_file_block_id_digits=len(str(file_block_id))
    pattern = r'\.{'+str(num_times_file_block_id_is_printed)+'}'

    match = re.search(pattern, new_string)

    if match and match.start() < index_file_block_id:
        dots_start_index = match.start()
        dots_end_index = match.end()
        swapped_string = (
            new_string[:dots_start_index] +
            ('-'+str(file_block_id)+'-') * num_times_file_block_id_is_printed +
            new_string[dots_end_index:index_file_block_id] +
            '.' * num_times_file_block_id_is_printed +
            new_string[index_file_block_id+(num_times_file_block_id_is_printed * (length_file_block_id_digits+2)):]
        )
        new_string=swapped_string

    return new_string

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")
