import os
import time

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "2012_input.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    matrix = [list(line.strip()) for line in content]

    sx, sy = get_pos(matrix, 'S')
    ex, ey = get_pos(matrix, 'E')

    directions = ((-1,0),(0,1),(1,0),(0,-1))
    direction=0

    traveled = dict()
    traveled[(sx, sy)] = len(traveled)+1
    while True:
        if (sx, sy) == (ex, ey):
            print(f"End destination found after {len(traveled)} steps ")
            break
        curr_dir = directions[direction % 4]
        fx, fy = sx + curr_dir[0], sy + curr_dir[1]
        if matrix[fx][fy] == '#' or (fx, fy) in traveled:
            direction+=1
        else:
            sx, sy = fx, fy
            traveled[(sx, sy)] = len(traveled)+1

    sx, sy = get_pos(matrix, 'S')

    directions = ((-2,0),(0,2),(2,0),(0,-2))

    cheats = dict()
    for step in traveled:
        for direction in directions:
            fx, fy = step[0]+ direction[0], step[1] + direction[1]
            if (fx, fy) in traveled and (step[0], step[1], fx, fy) not in cheats:
                diff = traveled[(fx, fy)] - traveled[(step[0], step[1])] - 2
                if diff >= 100:
                    cheats[(step[0], step[1], fx, fy)]=diff

    print(len(cheats))

def get_pos(matrix, char):
    for i in range(len(matrix)):
        for ii in range(len(matrix[i])):
            if matrix[i][ii] == char:
                return i, ii

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")