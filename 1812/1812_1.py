import os
import time
import sys
lowest_score_per_plot=list()
rows=0
cols=0
sys.setrecursionlimit(100000) 
def main():
    global rows, cols, lowest_score_per_plot
    os.chdir(os.path.dirname(__file__))
    file_path = "1812_input.txt"

    with open(file_path, "r") as file:
        content = file.read()
    lines = content.strip().split('\n')
    lines = lines[:1024]

    rows = 71
    cols = 71

    matrix = [['.' for _ in range(cols)] for _ in range(rows)]
    lowest_score_per_plot = [[-1 for _ in range(cols)] for _ in range(rows)]

    for line in lines:
        x_str, y_str = line.strip().split(',')
        x, y = int(x_str), int(y_str)
        matrix[y][x]='#'

    startpos=(0,0)

    eval(startpos, matrix, 0)

def eval(startpos, matrix, score):
    global lowest_score_per_plot
    
    if startpos[0] == rows -1 and startpos[1] == cols - 1:
        print(f'Lowest score so far = {score}')
        return
    
    score+=1

    if not lowest_score_per_plot[startpos[0]][startpos[1]] == -1 and score >= lowest_score_per_plot[startpos[0]][startpos[1]]:
        return
    else:
        lowest_score_per_plot[startpos[0]][startpos[1]] = score

    if startpos[0] +1 < rows and matrix[startpos[0] +1][startpos[1]] != '#':
        eval((startpos[0] +1, startpos[1]), matrix, score)
    
    if startpos[0] - 1 >= 0 and matrix[startpos[0] - 1][startpos[1]] != '#':
        eval((startpos[0] - 1, startpos[1]), matrix, score)

    if startpos[1] + 1 < cols  and matrix[startpos[0]][startpos[1]+1] != '#':
        eval((startpos[0], startpos[1]+1), matrix, score)

    if startpos[1] - 1 >= 0 and matrix[startpos[0]][startpos[1]-1] != '#':
        eval((startpos[0], startpos[1]-1), matrix, score)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")