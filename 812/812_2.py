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
                #Register both similar antenna's as antinodes
                register_antinode([i,ii])
                register_antinode(curr_pos)
                times=0
                while True:
                    times+=1
                    pot_antinode_row = curr_pos[0] + (row_diff * times)
                    pot_antinode_col = curr_pos[1] + (col_diff * times)
                    if 0 <= pot_antinode_row < len(matrix):
                        if 0 <= pot_antinode_col < len(matrix[0]):
                            register_antinode([pot_antinode_row, pot_antinode_col])
                        else:
                            break
                    else:
                        break

def register_antinode(antinode_pos):
    global antinodes_registered
    if not antinode_pos in antinodes_registered:
        antinodes_registered.append(antinode_pos)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")