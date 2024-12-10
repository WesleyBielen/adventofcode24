import os
import time
import copy

total_valid_routes = 0


def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "1012_input.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    matrix = [list(line.strip()) for line in content]
    trailheads_start_pos = []
    for i in range(len(matrix)):
        for ii in range(len(matrix[i])):
            if matrix[i][ii] == '0':
                trailheads_start_pos.append([i, ii])

    for i in range(len(trailheads_start_pos)):
        trailhead_start_pos = trailheads_start_pos[i]
        get_next_num(0, trailhead_start_pos, matrix)

    print(total_valid_routes)

def get_next_num(current_num, current_pos, matrix):
    current_num += 1
    global total_valid_routes
    if current_num == 10:
        total_valid_routes += 1
        return

    # Check North
    if current_pos[0] > 0:
        if matrix[current_pos[0] - 1][current_pos[1]] == str(current_num):
            new_pos = copy.deepcopy(current_pos)
            new_pos[0] -= 1
            get_next_num(current_num, new_pos, matrix)

    # Check East
    if current_pos[1] < len(matrix[0]) - 1:
        if matrix[current_pos[0]][current_pos[1] + 1] == str(current_num):
            new_pos = copy.deepcopy(current_pos)
            new_pos[1] += 1
            get_next_num(current_num, new_pos, matrix)

    # Check South
    if current_pos[0] < len(matrix) - 1:
        if matrix[current_pos[0] + 1][current_pos[1]] == str(current_num):
            new_pos = copy.deepcopy(current_pos)
            new_pos[0] += 1
            get_next_num(current_num, new_pos, matrix)

    # Check West
    if current_pos[1] > 0:
        if matrix[current_pos[0]][current_pos[1] - 1] == str(current_num):
            new_pos = copy.deepcopy(current_pos)
            new_pos[1] -= 1
            get_next_num(current_num, new_pos, matrix)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")