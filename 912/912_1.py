import re
import os
import time

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "912_input_sample.txt"

    with open(file_path, "r") as file:
        content = file.read()

    new_string = ""
    alt = False
    file_block_num=0
    for i in range(len(content)):
        if alt:
            new_string+=  str('.' * int(content[i]))
        else:
            new_string += str(str(file_block_num) * int(content[i]))
            file_block_num+=1
        alt = not alt
    print(new_string)
    for i in range(file_block_num, 0, -1):
        num_times_file_block_id_is_printed = int((content[(i*2)-2]))
        #print(f'File block ID {i-1} is printed {num_times_file_block_id_is_printed}')
        new_string = swap(i-1, num_times_file_block_id_is_printed, new_string)
        # Check if we still need to continue (eg. a '.' is still to be found in between digits)
        if not (re.search(r"(?<=\d)\.(?=\d)", new_string)):
            break

def swap(file_block_id, num_times_file_block_id_is_printed, new_string):
    length_new_string = len(new_string)
    for i in range(num_times_file_block_id_is_printed):
        if not (re.search(r"(?<=\d)\.(?=\d)", new_string)):
            break
        length_file_block_id_digits=len(str(file_block_id))
        pattern = r'\.{'+str(length_file_block_id_digits)+'}'

        match = re.search(pattern, new_string)

        if match:
            dots_start_index = match.start()
            dots_end_index = match.end()
            
            index_right = new_string.rfind(str(file_block_id))
            
            swapped_string = (
                new_string[:dots_start_index] +
                str(file_block_id) +
                new_string[dots_end_index:index_right]
            ).ljust(length_new_string, '.')
            
            print(f"Modified string: {swapped_string}")
            new_string=swapped_string
        else:
            print("No occurrence found.")
    return new_string

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")
