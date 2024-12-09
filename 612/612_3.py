import os
import time
import sys
import copy

sys.setrecursionlimit(1000000)
total_valid_crates=0
def main():
    os.chdir(os.path.dirname(__file__))
    file_path = '612_input.txt'

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
                        validate_new_crate(curr_pos[:], matrix, 1)
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
                        validate_new_crate(curr_pos[:], matrix, 2)
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
                        validate_new_crate(curr_pos[:], matrix, 3)
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
                        validate_new_crate(curr_pos[:], matrix, 0)
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
    crate_pos = curr_pos[:]
    m2 = copy.deepcopy(matrix)

    # Put new crate
    match travel % 4:
        case 0:
            crate_pos = [curr_pos[0],curr_pos[1]-1]
        case 1:
            crate_pos = [curr_pos[0]-1, curr_pos[1]]
        case 2:
            crate_pos = [curr_pos[0], curr_pos[1] + 1]
        case 3:
            crate_pos = [curr_pos[0]+1, curr_pos[1]]

    m2[crate_pos[0]][crate_pos[1]] = '#'

    while True:
        direction_found = False
        crate_found = False
        first_iter = True
        match travel % 4:
            case 0:
                # Going up
                while curr_pos[0] > 0:
                    curr_pos[0] -= 1
                    pos_to_check = m2[curr_pos[0]][curr_pos[1]]
                    if  pos_to_check == '#':
                        if not first_iter:
                            curr_pos[0] += 1
                            crate_found = True
                        break
                    if 'N' in pos_to_check:
                        direction_found = True
                        break
                    else:
                        m2[curr_pos[0]][curr_pos[1]] += 'N'

                    first_iter = False

                if direction_found:
                    #print_matrix(m2)
                    total_valid_crates += 1
                    print(
                        f'GU. New crate found at {crate_pos[0]} / {crate_pos[1]} This is number {total_valid_crates} '
                        f' While + was spotted at {curr_pos[0]} / {curr_pos[1]} ')
                    break
                elif crate_found:
                    travel+=1
                else:
                    break
            case 1:
                # Going right
                while curr_pos[1] < len(m2[0]) - 1:
                    curr_pos[1] += 1
                    pos_to_check = m2[curr_pos[0]][curr_pos[1]]
                    if pos_to_check == '#':
                        if not first_iter:
                            curr_pos[1] -= 1
                            crate_found = True
                        break
                    if 'E' in pos_to_check:
                        direction_found = True
                        break
                    else:
                        m2[curr_pos[0]][curr_pos[1]] += 'E'
                    first_iter = False

                if direction_found:
                    #print_matrix(m2)
                    total_valid_crates += 1
                    print(
                        f'GR. New crate found at {crate_pos[0]} / {crate_pos[1]} This is number {total_valid_crates} '
                        f' While + was spotted at {curr_pos[0]} / {curr_pos[1]} ')
                    break
                elif crate_found:
                    travel+=1
                else:
                    break
            case 2:
                # Going down
                while curr_pos[0] < len(m2) - 1:
                    curr_pos[0] += 1
                    pos_to_check = m2[curr_pos[0]][curr_pos[1]]
                    if pos_to_check == '#':
                        if not first_iter:
                            curr_pos[0] -= 1
                            crate_found = True
                        break

                    if 'S' in pos_to_check:
                        direction_found = True
                        break
                    else:
                        m2[curr_pos[0]][curr_pos[1]] += 'S'

                    first_iter = False

                if direction_found:
                    #print_matrix(m2)
                    total_valid_crates += 1
                    print(
                        f'GD. New crate found at {crate_pos[0]} / {crate_pos[1]} This is number {total_valid_crates} .'
                        f' While + was spotted at {curr_pos[0]} / {curr_pos[1]} ')
                    break
                elif crate_found:
                    travel+=1
                else:
                    break
            case 3:
                # Going left
                while curr_pos[1] > 0:
                    curr_pos[1] -= 1
                    pos_to_check = m2[curr_pos[0]][curr_pos[1]]
                    if pos_to_check == '#':
                        if not first_iter:
                            curr_pos[1] += 1
                            crate_found = True
                        break
                    if 'W' in pos_to_check:
                        direction_found = True
                        break
                    else:
                        m2[curr_pos[0]][curr_pos[1]] += 'W'
                    first_iter = False

                if direction_found:
                    #print_matrix(m2)
                    total_valid_crates += 1
                    print(
                        f'GL. New crate found at {crate_pos[0]} / {crate_pos[1]} This is number {total_valid_crates} '
                        f' While + was spotted at {curr_pos[0]} / {curr_pos[1]} ')
                    break
                elif crate_found:
                    travel+=1
                else:
                    break

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