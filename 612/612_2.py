import os
import time
import sys
import copy

sys.setrecursionlimit(1000000)
total_valid_crates=0
def main():
    os.chdir(os.path.dirname(__file__))
    file_path = 'raw_data.txt'

    with open(file_path, 'r') as file:
        content = file.readlines()

    matrix = [list(line.strip()) for line in content]

    curr_pos = determine_curr_pos(matrix)
    print(f'begin pos = {curr_pos}')
    matrix[curr_pos[0]][curr_pos[1]] = 'N'
    current_travel = 0
    total_travel = 1
    while True:
        obstacle_found = False
        match current_travel % 4:
            case 0:
                # Going up
                while curr_pos[0] > 0:
                    validate_traveled(curr_pos, matrix, 'N')
                    if matrix[curr_pos[0] - 1][curr_pos[1]] != '#':
                        validate_new_crate(curr_pos[:], matrix, current_travel)
                        if matrix[curr_pos[0] - 1][curr_pos[1]] == '.':
                            total_travel += 1
                        curr_pos[0] -= 1
                    else:
                        obstacle_found = True
                        break
            case 1:
                # Going right
                while curr_pos[1] < len(matrix[0]) - 1:
                    validate_traveled(curr_pos, matrix, 'E')
                    if matrix[curr_pos[0]][curr_pos[1] + 1] != '#':
                        validate_new_crate(curr_pos[:], matrix, current_travel)
                        if matrix[curr_pos[0]][curr_pos[1] + 1] == '.':
                            total_travel += 1
                        curr_pos[1] += 1
                    else:
                        obstacle_found = True
                        break
            case 2:
                # Going down
                while curr_pos[0] < len(matrix) - 1:
                    validate_traveled(curr_pos, matrix, 'S')
                    if matrix[curr_pos[0] + 1][curr_pos[1]] != '#':
                        validate_new_crate(curr_pos[:], matrix, current_travel)
                        if matrix[curr_pos[0] + 1][curr_pos[1]] == '.':
                            total_travel += 1
                        curr_pos[0] += 1
                    else:
                        obstacle_found = True
                        break
            case 3:
                # Going left
                while curr_pos[1] > 0:
                    validate_traveled(curr_pos, matrix, 'W')
                    if matrix[curr_pos[0]][curr_pos[1] - 1] != '#':
                        validate_new_crate(curr_pos[:], matrix, current_travel)
                        if matrix[curr_pos[0]][curr_pos[1] - 1] == '.':
                            total_travel += 1
                        curr_pos[1] -= 1
                    else:
                        obstacle_found = True
                        break

        if not obstacle_found:
            break
        current_travel += 1

    for line in matrix:
       print(' '.join(line))
    print(total_travel)
    print(total_valid_crates)

def validate_new_crate(curr_pos, matrix, travel):
    global total_valid_crates
    crate_pos = copy.deepcopy(curr_pos)
    virtual_pos = copy.deepcopy(curr_pos)
    m2 = copy.deepcopy(matrix)
    travel_virtual = copy.deepcopy(travel)
    
    # Put new crate
    match travel_virtual % 4:
        case 0:
            crate_pos[0]-=1
        case 1:
            crate_pos[1] += 1
        case 2:
            crate_pos[0] += 1
        case 3:
            crate_pos[1] -= 1

    m2[crate_pos[0]][crate_pos[1]] = '#'
    
    while True:
        travel_virtual+=1
        crate_found=False
        first_iter=True
        match travel_virtual % 4:
            case 0:
                # Going up
                while virtual_pos[0] > 0:
                    if not first_iter:
                        crate_found, direction_found = validate_is_traveled(virtual_pos, m2, 'N')
                        if crate_found or direction_found:
                            break
                    first_iter=False
                    validate_traveled(virtual_pos, m2, 'N')
                    virtual_pos[0] -= 1
            case 1:
                # Going right
                while virtual_pos[1] < len(m2[0]) - 1:
                    if not first_iter:
                        crate_found, direction_found = validate_is_traveled(virtual_pos, m2, 'E')
                        if crate_found or direction_found:
                            break
                    first_iter = False
                    validate_traveled(virtual_pos, m2, 'E')
                    virtual_pos[1] += 1
            case 2:
                # Going down
                while virtual_pos[0] < len(m2) - 1:
                    if not first_iter:
                        crate_found, direction_found = validate_is_traveled(virtual_pos, m2, 'S')
                        if crate_found or direction_found:
                            break
                    first_iter = False
                    validate_traveled(virtual_pos, m2, 'S')
                    virtual_pos[0] += 1
            case 3:
                # Going left
                while virtual_pos[1] > 0:
                    if not first_iter:
                        crate_found, direction_found = validate_is_traveled(virtual_pos, m2, 'W')
                        if crate_found or direction_found:
                            break
                    first_iter = False
                    validate_traveled(virtual_pos, m2, 'W')
                    virtual_pos[1] -= 1

        if not crate_found:
            break
                   
def validate_is_traveled(pos, matrix, direction):
    global total_valid_crates
    crate_found = False
    direction_found = False
    if matrix[pos[0]][pos[1]] == '#':
        crate_found = True
    elif direction in matrix[pos[0]][pos[1]]:
        total_valid_crates+=1
        direction_found = True
    return crate_found, direction_found

def validate_traveled(curr_pos, matrix, direction):
    matrix[curr_pos[0]][curr_pos[1]] += direction

def print_matrix(matrix):
    for line in matrix:
       print(' '.join(line))

def determine_curr_pos(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    for i in range(num_rows):
        for ii in range(num_columns):
            if matrix[i][ii] == '^':
                return [i, ii]


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Program completed in {elapsed_time:.5f} seconds')