import os
import time
import copy
import sys

directions = ['N','E','S','W']
startpos=None
endpos=None
firstiter=True
lowest_score=0
lowest_score_per_plot=dict()
set_plots_lowest_score=set()
sys.setrecursionlimit(10000000) 
def main():
    global startpos, endpos, lowest_score_per_plot, set_plots_lowest_score
    os.chdir(os.path.dirname(__file__))
    file_path = "1612_input.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    matrix = [list(line.strip()) for line in content]

    for i in range(len(matrix)):
        for ii in range(len(matrix[i])):
            if 'S' == matrix[i][ii]:
                startpos=(i,ii)
                continue
            if 'E' == matrix[i][ii]:
                endpos=(i,ii)
    
    lowest_score_per_plot['N']=[['-1' for _ in row] for row in matrix]
    lowest_score_per_plot['E']=[['-1' for _ in row] for row in matrix]
    lowest_score_per_plot['S']=[['-1' for _ in row] for row in matrix]
    lowest_score_per_plot['W']=[['-1' for _ in row] for row in matrix]
    print(f'Startpos = {startpos} / Endpos = {endpos}')
    eval(startpos, matrix, 'E','E', 0, [])
    print(f'Amount of tiles: {len(set_plots_lowest_score)+1}')

def eval(pos, matrix, previous_direction, direction, totalscore, plot_traveled):
    global firstiter, lowest_score, lowest_score_per_plot, set_plots_lowest_score
    if pos == startpos and not firstiter:
        return
    if pos in plot_traveled:
        return
    firstiter = False
    if pos == endpos:
        print(f'Endpos found. Score = {totalscore}. Traveled is {plot_traveled}')
        if totalscore < lowest_score or lowest_score == 0:
            set_plots_lowest_score = set()
            set_plots_lowest_score.update(plot_traveled)
            lowest_score = totalscore
        elif totalscore == lowest_score:
            set_plots_lowest_score.update(plot_traveled)
        print(f'Lowest score so far is {lowest_score}')
        return
    
    plot_traveled.append(pos)
    score=calc_rotation(previous_direction, direction)
    if score > 1001:
        return
    else:
        totalscore+=score

    if totalscore > 99488:
        return
    
    if not int(lowest_score_per_plot[direction][pos[0]][pos[1]]) == -1 and totalscore > int(lowest_score_per_plot[direction][pos[0]][pos[1]]):
        return
    else:
         lowest_score_per_plot[direction][pos[0]][pos[1]] = totalscore

    already_traveled = len(plot_traveled)

    if not matrix[pos[0]][pos[1]+1] == "#":
            eval((pos[0],pos[1]+1), matrix, direction, 'E', totalscore, plot_traveled)

    plot_traveled = plot_traveled[:already_traveled]
    if not matrix[pos[0]+1][pos[1]] == "#":
        eval((pos[0]+1,pos[1]), matrix, direction, 'S', totalscore, plot_traveled)

    plot_traveled = plot_traveled[:already_traveled]
    if not matrix[pos[0]][pos[1]-1] == "#":
        eval((pos[0],pos[1]-1), matrix, direction,'W', totalscore, plot_traveled)

    plot_traveled = plot_traveled[:already_traveled]
    if not matrix[pos[0]-1][pos[1]] == "#":
        eval((pos[0]-1,pos[1]), matrix, direction, 'N', totalscore, plot_traveled)

def calc_rotation(curr_dir, new_dir):
    if curr_dir == new_dir:
        return 1
    if abs(directions.index(curr_dir) - directions.index(new_dir)) == 2:
        return 2001
    return 1001
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")