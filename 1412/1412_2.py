import os
import time
import re
from sympy import symbols, Eq, solve

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

    i=0
    while True:
        new_pos=[]
        i+=1
        for p_values, v_values in results:
            new_place_after_col=None
            new_place_after_row=None
            if v_values[0] < 0:
                new_place_after_col = (p_values[0] + (i * (cols + v_values[0]))) % cols
            else:
                new_place_after_col = (p_values[0] + (i * v_values[0])) % cols

            if v_values[1] < 0:
                new_place_after_row = (p_values[1] + (i * (rows + v_values[1]))) % rows
            else:
                new_place_after_row = (p_values[1] + (i * v_values[1])) % rows

            new_pos.append([new_place_after_row, new_place_after_col])

        set_of_tuples = {tuple(lst) for lst in new_pos}
        if len(set_of_tuples) == len(new_pos):
            print(f'Found pattern after {i} seconds.')
            xmas_tree= [[' ' for _ in range(cols)] for _ in range(rows)]
            for pos in new_pos:
                xmas_tree[pos[0]][pos[1]]='X'

            for i in range(len(xmas_tree)):
                print(' '.join(xmas_tree[i]))
            return

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")