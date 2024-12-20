import os
import time
import re

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "1512_input_matrix.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    matrix = [list(line.strip()) for line in content]

    #print(matrix)

    file_path = "1512_input_moves.txt"
    with open(file_path, "r") as file:
        content = file.read()

    moves = list(content)

    pos=[]
    for i in range(len(matrix)):
        for ii in range(len(matrix[i])):
            if matrix[i][ii]=='@':
                pos=[i,ii]
                break

    for i in range(len(moves)):
        move = moves[i]
        match move:
            case '<':
                if pos[1] > 1 and not matrix[pos[0]][pos[1]-1] == '#':
                    if matrix[pos[0]][pos[1]-1] == 'O':
                        free_pos = get_next_free_spot(pos, matrix, '<')
                        if free_pos:
                            matrix[pos[0]][pos[1]] = '.'
                            pos[1] -= 1
                            matrix[free_pos[0]][free_pos[1]]='O'
                            matrix[pos[0]][pos[1]]='@'
                    else:
                        matrix[pos[0]][pos[1]] = '.'
                        pos[1]-=1
                        matrix[pos[0]][pos[1]] = '@'
                else:
                    continue
            case '>':
                if pos[1] < (len(matrix[0]) -2) and not matrix[pos[0]][pos[1] + 1] == '#':
                    if matrix[pos[0]][pos[1] + 1] == 'O':
                        free_pos = get_next_free_spot(pos, matrix, '>')
                        if free_pos:
                            matrix[pos[0]][pos[1]] = '.'
                            pos[1] += 1
                            matrix[free_pos[0]][free_pos[1]] = 'O'
                            matrix[pos[0]][pos[1]] = '@'
                    else:
                        matrix[pos[0]][pos[1]] = '.'
                        pos[1] += 1
                        matrix[pos[0]][pos[1]] = '@'
                else:
                    continue
            case 'v':
                if pos[0] < (len(matrix)-2) and not matrix[pos[0]+1][pos[1]] == '#':
                    if matrix[pos[0]+1][pos[1]] == 'O':
                        free_pos = get_next_free_spot(pos, matrix, 'v')
                        if free_pos:
                            matrix[pos[0]][pos[1]] = '.'
                            pos[0] += 1
                            matrix[free_pos[0]][free_pos[1]] = 'O'
                            matrix[pos[0]][pos[1]] = '@'
                    else:
                        matrix[pos[0]][pos[1]] = '.'
                        pos[0] += 1
                        matrix[pos[0]][pos[1]] = '@'
                else:
                    continue
            case '^':
                if pos[0] > 1 and not matrix[pos[0]-1][pos[1] ] == '#':
                    if matrix[pos[0]-1][pos[1]] == 'O':
                        free_pos = get_next_free_spot(pos, matrix, '^')
                        if free_pos:
                            matrix[pos[0]][pos[1]] = '.'
                            pos[0] -= 1
                            matrix[free_pos[0]][free_pos[1]] = 'O'
                            matrix[pos[0]][pos[1]] = '@'
                    else:
                        matrix[pos[0]][pos[1]] = '.'
                        pos[0] -= 1
                        matrix[pos[0]][pos[1]] = '@'
                else:
                    continue
        # print(f'Case after move {move}')
        # for line in matrix:
        #     for char in line:
        #         print(char, end=' ')  # No space
        #     print()

    total_score=0
    for i in range(len(matrix)):
        for ii in range(len(matrix[0])):
            if matrix[i][ii] == 'O':
                total_score+= (i*100)+ii
    print(total_score)

def get_next_free_spot(pos, matrix, direction) -> list:
    free_pos=pos[:]
    match direction:
        case '<':
            while True:
                free_pos[1]-=1
                if free_pos[1] > 0 and not matrix[free_pos[0]][free_pos[1]] == '#':
                    if not matrix[free_pos[0]][free_pos[1]] == 'O':
                        return free_pos
                else:
                    return []
        case '>':
            while True:
                free_pos[1] += 1
                if free_pos[1] < (len(matrix)-1) and not matrix[free_pos[0]][free_pos[1]] == '#':
                    if not matrix[free_pos[0]][free_pos[1]] == 'O':
                        return free_pos
                else:
                    return []
        case 'v':
            while True:
                free_pos[0] += 1
                if free_pos[0] < (len(matrix[0])-1) and not matrix[free_pos[0]][free_pos[1]] == '#':
                    if not matrix[free_pos[0]][free_pos[1]] == 'O':
                        return free_pos
                else:
                    return []
        case '^':
            while True:
                free_pos[0] -= 1
                if free_pos[0] > 0 and not matrix[free_pos[0]][free_pos[1]] == '#':
                    if not matrix[free_pos[0]][free_pos[1]] == 'O':
                        return free_pos
                else:
                    return []

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")