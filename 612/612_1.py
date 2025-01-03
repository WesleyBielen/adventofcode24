import os
import time

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = '612_input.txt'

    with open(file_path, 'r') as file:
        content = file.readlines()

    matrix = [list(line.strip()) for line in content]
    
    curr_pos = determine_curr_pos(matrix)
    current_travel = 0
    traveled=set()
    traveled.add((curr_pos[0], curr_pos[1]))
    while True:
        obstacle_found = False
        match current_travel % 4:
            case 0:
                # Going up
                while curr_pos[0] > 0:
                    if matrix[curr_pos[0]-1][curr_pos[1]] != '#':
                        traveled.add((curr_pos[0], curr_pos[1]))
                        matrix[curr_pos[0]-1][curr_pos[1]] = '^'
                        curr_pos[0]-=1
                    else:
                        obstacle_found=True
                        break
            case 1:
                # Going right
                while curr_pos[1] < len(matrix[0])-1:
                    if matrix[curr_pos[0]][curr_pos[1]+1] != '#':
                        traveled.add((curr_pos[0], curr_pos[1]))
                        matrix[curr_pos[0]][curr_pos[1]+1] = '>'
                        curr_pos[1]+=1
                    else:
                        obstacle_found=True
                        break
            case 2:
                # Going down
                while curr_pos[0] < len(matrix)-1:
                    if matrix[curr_pos[0]+1][curr_pos[1]] != '#':
                        traveled.add((curr_pos[0], curr_pos[1]))
                        matrix[curr_pos[0]+1][curr_pos[1]] = 'v'
                        curr_pos[0]+=1
                    else:
                        obstacle_found=True
                        break
            case 3:
                # Going left
                while curr_pos[1] > 0:
                    if matrix[curr_pos[0]][curr_pos[1]-1] != '#':
                        traveled.add((curr_pos[0], curr_pos[1]))
                        matrix[curr_pos[0]][curr_pos[1]-1] = '<'
                        curr_pos[1]-=1
                    else:
                        obstacle_found=True
                        break

        if not obstacle_found:
            break
        current_travel+=1

    for line in matrix:
       print(' '.join(line))
    print(len(traveled)+1)

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