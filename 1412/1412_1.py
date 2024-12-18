import os
import time
import re

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "1412_input.txt"

    rows=103
    cols=101
    row_to_ignore = rows // 2
    col_to_ignore = cols // 2
    with open(file_path, "r") as file:
        content = file.read()

    pattern = r"p=([-]?\d+),\s*([-]?\d+)\s+v=([-]?\d+),\s*([-]?\d+)"

    matches = re.findall(pattern, content)
    results = [(tuple(map(int, match[:2])), tuple(map(int, match[2:]))) for match in matches]

    sq_ne=0
    sq_nw=0
    sq_se=0
    sq_sw=0
    for p_values, v_values in results:
        new_place_after_col=None
        new_place_after_row=None
        if v_values[0] < 0:
            new_place_after_col = (p_values[0] + (100 * (cols + v_values[0]))) % cols
        else:
            new_place_after_col = (p_values[0] + (100 * v_values[0])) % cols

        if v_values[1] < 0:
            new_place_after_row = (p_values[1] + (100 * (rows + v_values[1]))) % rows
        else:
            new_place_after_row = (p_values[1] + (100 * v_values[1])) % rows

        if new_place_after_row == row_to_ignore or new_place_after_col == col_to_ignore:
            continue

        if new_place_after_row < row_to_ignore:
            #North
            if new_place_after_col < col_to_ignore:
                sq_nw +=1
            else:
                sq_ne +=1
        else:
            #South
            if new_place_after_col < col_to_ignore:
                sq_sw +=1
            else:
                sq_se +=1

    safety_factor = sq_ne * sq_nw * sq_se * sq_sw
    print(safety_factor)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")