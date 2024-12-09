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
    #matrix[curr_pos[0]][curr_pos[1]] = 'N'
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
    virtual_travel = copy.deepcopy(travel)
    m2 = copy.deepcopy(matrix)

    going_up = list()
    going_right = list()
    going_down = list()
    going_left = list()

    # Put new crate
    match virtual_travel % 4:
        case 0:
            crate_pos[0]-=1
            going_up.append((crate_pos[0], crate_pos[1]))
        case 1:
            crate_pos[1] += 1
            going_right.append((crate_pos[0], crate_pos[1]))
        case 2:
            crate_pos[0] += 1
            going_down.append((crate_pos[0], crate_pos[1]))
        case 3:
            crate_pos[1] -= 1
            going_left.append((crate_pos[0], crate_pos[1]))

    #print(going_left)
    m2[crate_pos[0]][crate_pos[1]] = '#'

    print(f'Evaluating crate at {crate_pos[0]}/{crate_pos[1]} - Travel is {virtual_travel}')

    while True:
        virtual_travel+=1
        first_iter=True
        crate_found=False
        match virtual_travel % 4:
            case 0:
                # Going up
                while virtual_pos[0] > 0:
                    virtual_pos[0] -= 1
                    if (virtual_pos[0],virtual_pos[1]) in going_up:
                        print(f'GU Loop found! {virtual_pos} starting from {curr_pos}. Crate at {crate_pos}')
                        total_valid_crates += 1
                        break
                    elif m2[virtual_pos[0]][virtual_pos[1]] == '#':
                        if first_iter:
                            break
                        else:
                            crate_found = True
                            going_up.append((virtual_pos[0], virtual_pos[1]))

                            print(f'GU actual crate found at {virtual_pos}')
                            virtual_pos[0] += 1
                            break
                    first_iter = False

            case 1:
                # Going right
                while virtual_pos[1] < len(m2[0]) - 1:
                    virtual_pos[1] += 1
                    if (virtual_pos[0],virtual_pos[1]) in going_right:
                        print(f'GR Loop found! {virtual_pos} starting from {curr_pos} Crate at {crate_pos}')
                        total_valid_crates += 1
                        break
                    elif m2[virtual_pos[0]][virtual_pos[1]] == '#':
                        if first_iter:
                            break
                        else:
                            crate_found = True
                            print(f'GR actual crate found at {virtual_pos}')
                            going_right.append((virtual_pos[0], virtual_pos[1]))
                            virtual_pos[1] -= 1
                            break
                    first_iter = False

            case 2:
                # Going down
                while virtual_pos[0] < len(m2) - 1:
                    virtual_pos[0] += 1
                    if (virtual_pos[0],virtual_pos[1]) in going_down:
                        print(f'GD Loop found! {virtual_pos} starting from {curr_pos} Crate at {crate_pos}')
                        total_valid_crates += 1
                        break
                    elif m2[virtual_pos[0]][virtual_pos[1]] == '#':
                        if first_iter:
                            break
                        else:
                            crate_found = True
                            going_down.append((virtual_pos[0], virtual_pos[1]))
                            print(f'GD actual crate found at {virtual_pos}')
                            virtual_pos[0] -= 1
                            break
                    first_iter = False

            case 3:
                # Going left
                while virtual_pos[1] > 0:
                    virtual_pos[1] -= 1
                    if (virtual_pos[0],virtual_pos[1]) in going_left:
                        print(f'GL Loop found! {virtual_pos} starting from {curr_pos} Crate at {crate_pos}')
                        total_valid_crates+=1
                        break
                    elif m2[virtual_pos[0]][virtual_pos[1]] == '#':
                        if first_iter:
                            break
                        else:
                            print(f'GL actual crate found at {virtual_pos}')
                            crate_found = True
                            going_left.append((virtual_pos[0], virtual_pos[1]))
                            virtual_pos[1] += 1
                            break
                    first_iter = False

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