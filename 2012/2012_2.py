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

    traveled = dict()
    direction=0
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
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

    total_cheats=0
    for step in traveled:
        for ostep in traveled:
            steps = abs(step[0] - ostep[0]) + abs(step[1] - ostep[1])
            if steps <= 20:
                diff = traveled[ostep] - traveled[step] - steps
                if diff >= 100:
                    total_cheats+=1

    print(total_cheats)

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