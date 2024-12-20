import os
import time
import copy

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "1512_input_matrix.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    matrix = [list(line.strip()) for line in content]

    new_matrix=[]
    #print(matrix)

    file_path = "1512_input_moves.txt"
    with open(file_path, "r") as file:
        content = file.read()

    moves = list(content)

    for i in range(len(matrix)):
        new_matrix.append([])
        for ii in range(len(matrix[i])):
            if matrix[i][ii]=='@':
                new_matrix[i].append('@')
                new_matrix[i].append('.')
            if matrix[i][ii]=='#':
                new_matrix[i].append('#')
                new_matrix[i].append('#')
            if matrix[i][ii]=='.':
                new_matrix[i].append('.')
                new_matrix[i].append('.')
            if matrix[i][ii]=='O':
                new_matrix[i].append('[')
                new_matrix[i].append(']')

    for line in new_matrix:
        for char in line:
                print(char, end=' ') 
        print()

    pos=[]
    for i in range(len(new_matrix)):
        for ii in range(len(new_matrix[i])):
            if new_matrix[i][ii]=='@':
                pos=[i,ii]
                break

    for i in range(len(moves)):
        move = moves[i]
        match move:
            case '<':
                if pos[1] > 1 and not new_matrix[pos[0]][pos[1]-1] == '#':
                    if new_matrix[pos[0]][pos[1]-1] == ']':
                        free_pos = get_next_free_spot((pos[0],pos[1]), new_matrix, '<')
                        if free_pos:
                            move_boxes(free_pos, new_matrix, 0, -1, pos)
                            pos[1]-=1
                    else:
                        new_matrix[pos[0]][pos[1]] = '.'
                        pos[1]-=1
                        new_matrix[pos[0]][pos[1]] = '@'
                else:
                    continue
            case '>':
                if pos[1] < (len(new_matrix[0]) -2) and not new_matrix[pos[0]][pos[1] + 1] == '#':
                    if new_matrix[pos[0]][pos[1] + 1] == '[':
                        free_pos = get_next_free_spot((pos[0],pos[1]), new_matrix, '>')
                        if free_pos:
                            move_boxes(free_pos, new_matrix, 0, 1, pos)
                            pos[1] += 1
                    else:
                        new_matrix[pos[0]][pos[1]] = '.'
                        pos[1] += 1
                        new_matrix[pos[0]][pos[1]] = '@'
                else:
                    continue
            case 'v':
                if pos[0] < (len(new_matrix)-2) and not new_matrix[pos[0]+1][pos[1]] == '#':
                    if new_matrix[pos[0]+1][pos[1]] in ('[',']'):
                        free_pos = get_next_free_spot((pos[0],pos[1]), new_matrix, 'v')
                        if free_pos:
                            move_boxes(free_pos, new_matrix, 1, 0, pos)
                            pos[0] += 1
                    else:
                        new_matrix[pos[0]][pos[1]] = '.'
                        pos[0] += 1
                        new_matrix[pos[0]][pos[1]] = '@'
                else:
                    continue
            case '^':
                if pos[0] > 1 and not new_matrix[pos[0]-1][pos[1] ] == '#':
                    if new_matrix[pos[0]-1][pos[1]] in ('[',']'):
                        free_pos = get_next_free_spot((pos[0],pos[1]), new_matrix, '^')
                        if free_pos:
                           move_boxes(free_pos, new_matrix, -1, 0, pos)
                           pos[0] -= 1
                    else:
                        new_matrix[pos[0]][pos[1]] = '.'
                        pos[0] -= 1
                        new_matrix[pos[0]][pos[1]] = '@'
                else:
                    continue
    """         print(f'Case after move {move}')
        for line in new_matrix:
            for char in line:
               print(char, end=' ')  # No space
            print() """

    total_score=0
    for i in range(len(new_matrix)):
        for ii in range(len(new_matrix[0])):
            if new_matrix[i][ii] == '[':
                total_score+= (i*100)+ii
    print(total_score)

def move_boxes(boxes, matrix, row_jump, col_jump, curr_pos):
    matrix_temp = copy.deepcopy(matrix)
    moved_to = set()
    for pos in boxes:
        matrix[pos[0]+row_jump][pos[1]+col_jump]=matrix_temp[pos[0]][pos[1]]
        moved_to.add((pos[0]+row_jump,pos[1]+col_jump))

    for pos in boxes:
        if not pos in moved_to:
            matrix[pos[0]][pos[1]]='.'

def get_next_free_spot(pos, matrix, direction) -> list:
    boxes=set()
    boxes.add(pos)
    match direction:
        case '<':
            to_explore = boxes.copy()
            while True:
                for temp_pos in list(to_explore):
                    if matrix[temp_pos[0]][temp_pos[1]-1] in ('[',']'):
                        boxes.add((temp_pos[0], temp_pos[1]-1))
                        to_explore.add((temp_pos[0], temp_pos[1]-1))
                    elif matrix[temp_pos[0]][temp_pos[1]-1] == '#':
                        return set()
                    to_explore.remove(temp_pos)
                if not to_explore:
                    return boxes
            
        case '>':
            to_explore = boxes.copy()
            while True:
                for temp_pos in list(to_explore):
                    if matrix[temp_pos[0]][temp_pos[1]+1] in ('[',']'):
                        boxes.add((temp_pos[0], temp_pos[1]+1))
                        to_explore.add((temp_pos[0], temp_pos[1]+1))
                    elif matrix[temp_pos[0]][temp_pos[1]+1] == '#':
                        return set()
                    to_explore.remove(temp_pos) 
                if not to_explore:
                    return boxes
        case 'v':
            to_explore = boxes.copy()
            while True:
                for temp_pos in list(to_explore):
                    if matrix[temp_pos[0]+1][temp_pos[1]] == '[':
                        boxes.add((temp_pos[0]+1, temp_pos[1]))
                        to_explore.add((temp_pos[0]+1, temp_pos[1]))
                        boxes.add((temp_pos[0]+1, temp_pos[1]+1))
                        to_explore.add((temp_pos[0]+1, temp_pos[1]+1))
                    elif matrix[temp_pos[0]+1][temp_pos[1]] == ']':
                        boxes.add((temp_pos[0]+1, temp_pos[1]))
                        to_explore.add((temp_pos[0]+1, temp_pos[1]))
                        boxes.add((temp_pos[0]+1, temp_pos[1]-1))
                        to_explore.add((temp_pos[0]+1, temp_pos[1]-1))
                    elif matrix[temp_pos[0]+1][temp_pos[1]] == '#':
                        return set()
                    to_explore.remove(temp_pos)
                if not to_explore:
                    return boxes

        case '^':
            to_explore = boxes.copy()
            while True:
                for temp_pos in list(to_explore):
                    if matrix[temp_pos[0]-1][temp_pos[1]] == '[':
                        boxes.add((temp_pos[0]-1, temp_pos[1]))
                        to_explore.add((temp_pos[0]-1, temp_pos[1]))
                        boxes.add((temp_pos[0]-1, temp_pos[1]+1))
                        to_explore.add((temp_pos[0]-1, temp_pos[1]+1))
                    elif matrix[temp_pos[0]-1][temp_pos[1]] == ']':
                        boxes.add((temp_pos[0]-1, temp_pos[1]))
                        to_explore.add((temp_pos[0]-1, temp_pos[1]))
                        boxes.add((temp_pos[0]-1, temp_pos[1]-1))
                        to_explore.add((temp_pos[0]-1, temp_pos[1]-1))
                    elif matrix[temp_pos[0]-1][temp_pos[1]] == '#':
                        return set()
                    to_explore.remove(temp_pos)
                if not to_explore:
                    return boxes

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")