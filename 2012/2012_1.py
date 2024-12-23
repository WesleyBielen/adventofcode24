import os
import time

rows=cols=0
sx = sy = 0
ex = ey = 0
def main():
    global rows, cols, sx, sy, ex, ey
    os.chdir(os.path.dirname(__file__))
    file_path = "2012_input_sample.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    matrix = [list(line.strip()) for line in content]

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(len(matrix)):
        for ii in range(len(matrix[i])):
            if matrix[i][ii] == 'S':
                sx, sy = i, ii
            elif matrix[i][ii] == 'E':
                ex, ey = i, ii

    print(f'Startpos = {sx} / {sy}')
    print(f'Endpos = {ex} / {ey}')

    directions = ((1,0),(0,1),(-1,0),(0,-1))
    direction=0

    while True:
        sx, sy += directions[0][0], directions[0][1]
if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")