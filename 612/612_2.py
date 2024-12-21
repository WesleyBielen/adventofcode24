import os
import time


def main():
    os.chdir(os.path.dirname(__file__))
    file_path = '612_input.txt'

    with open(file_path, 'r') as file:
        content = file.readlines()

    matrix = [list(line.strip()) for line in content]

    row, column = determine_curr_pos(matrix)
    current_travel = 0
    traveled = set()
    traveled.add((row, column))
    while True:
        obstacle_found = False
        match current_travel % 4:
            case 0:
                # Going up
                while row > 0:
                    if matrix[row - 1][column] != '#':
                        traveled.add((row, column))
                        row -= 1
                    else:
                        obstacle_found = True
                        break
            case 1:
                # Going right
                while column < len(matrix[0]) - 1:
                    if matrix[row][column + 1] != '#':
                        traveled.add((row, column))
                        column += 1
                    else:
                        obstacle_found = True
                        break
            case 2:
                # Going down
                while row < len(matrix) - 1:
                    if matrix[row + 1][column] != '#':
                        traveled.add((row, column))
                        row += 1
                    else:
                        obstacle_found = True
                        break
            case 3:
                # Going left
                while column > 0:
                    if matrix[row][column - 1] != '#':
                        traveled.add((row, column))
                        column -= 1
                    else:
                        obstacle_found = True
                        break

        if not obstacle_found:
            print(f'Adding last position {row} / {column}')
            traveled.add((row, column))
            break
        current_travel += 1

    total_crate_loops=0
    for item in traveled:
        loop_traveled=set()
        row, column = determine_curr_pos(matrix)
        if item[0]==row and item[1]==column:
            continue

        current_travel = 0
        matrix[item[0]][item[1]]='#'

        loop_found=False
        while True:
            obstacle_found = False
            match current_travel % 4:
                case 0:
                    # Going up
                    while row > 0:
                        if (row, column, 0) in loop_traveled:
                            loop_found = True
                            break
                        else:
                            loop_traveled.add((row, column, 0))
                        if matrix[row - 1][column] != '#':
                            row -= 1
                        else:
                            obstacle_found = True
                            break
                case 1:
                    # Going right
                    while column < len(matrix[0]) - 1:
                        if (row, column, 1) in loop_traveled:
                            loop_found = True
                            break
                        else:
                            loop_traveled.add((row, column, 1))
                        if matrix[row][column + 1] != '#':
                            column += 1
                        else:
                            obstacle_found = True
                            break
                case 2:
                    # Going down
                    while row < len(matrix) - 1:
                        if (row, column, 2) in loop_traveled:
                            loop_found = True
                            break
                        else:
                            loop_traveled.add((row, column, 2))
                        if matrix[row + 1][column] != '#':
                            row += 1
                        else:
                            obstacle_found = True
                            break
                case 3:
                    # Going left
                    while column > 0:
                        if (row, column, 3) in loop_traveled:
                            loop_found = True
                            break
                        else:
                            loop_traveled.add((row, column, 3))
                        if matrix[row][column - 1] != '#':
                            column -= 1
                        else:
                            obstacle_found = True
                            break

            if loop_found:
                total_crate_loops+=1
                break
            if not obstacle_found:
                break
            current_travel += 1

        matrix[item[0]][item[1]] = '.'
    print(total_crate_loops)

def determine_curr_pos(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    for i in range(num_rows):
        for ii in range(num_columns):
            if matrix[i][ii] == '^':
                return i, ii


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Program completed in {elapsed_time:.5f} seconds')