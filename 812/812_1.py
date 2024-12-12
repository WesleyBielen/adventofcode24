import os
import time
import copy

antinodes_registered = []
def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "812_input.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    matrix = [list(line.strip()) for line in content]
    for i in range(len(matrix)):
        for ii in range(len(matrix[i])):
            if not matrix[i][ii] == '.':
                look_for_similar_antenna([i,ii], matrix, matrix[i][ii])
    print(f'Amount of antinodes = {len(antinodes_registered)}')
    print(antinodes_registered)

def look_for_similar_antenna(curr_pos, matrix, antenna):
    global antinodes_registered
    for i in range(len(matrix)):
        for ii in range(len(matrix[i])):
            if i == curr_pos[0] and ii == curr_pos[1]:
                continue
            if matrix[i][ii] == antenna:
                row_diff = curr_pos[0] - i
                col_diff = curr_pos[1] - ii
                pot_antinode_row= curr_pos[0] + row_diff
                pot_antinode_col = curr_pos[1] + col_diff
                if 0 <= pot_antinode_row < len(matrix):
                    if 0 <= pot_antinode_col < len(matrix[0]):
                        if [pot_antinode_row, pot_antinode_col] not in antinodes_registered:
                            antinodes_registered.append([pot_antinode_row, pot_antinode_col])

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")