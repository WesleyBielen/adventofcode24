import os
import time

cheats=dict()
traveled=dict()
evaluated=set()
directions = ((-1,0),(0,1),(1,0),(0,-1))
def main():
    global traveled, cheats, evaluated
    os.chdir(os.path.dirname(__file__))
    file_path = "2012_input_sample.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    matrix = [list(line.strip()) for line in content]

    sx, sy = get_pos(matrix, 'S')
    ex, ey = get_pos(matrix, 'E')

    direction=0
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


    for step in traveled:
        evaluated=set()
        print(f'Searching step {step}')
        search(matrix, 0, step, step)

    print(len(cheats))

def search(matrix, i, plot, newplot):
    global traveled, cheats, evaluated
    i+=1
    if i > 20:
        return

    fx, fy = newplot[0]+ directions[0][0], newplot[1] + directions[0][1]

    if (fx, fy) in traveled and (plot[0], plot[1], fx, fy) not in cheats:
        diff = traveled[(fx, fy)] - traveled[plot] - i
        if diff >= 50:
            cheats[(plot[0], plot[1], fx, fy)]=diff
            return
        
    elif fx > 0 and matrix[fx][fy]=="#":
        search(matrix, i, plot, (fx, fy))

    fx, fy = newplot[0]+ directions[1][0], newplot[1] + directions[1][1]
    if (fx, fy) in traveled and (plot[0], plot[1], fx, fy) not in cheats:
        diff = traveled[(fx, fy)] - traveled[plot] - i
        if diff >= 50:
            cheats[(plot[0], plot[1], fx, fy)]=diff
            return
        
    elif fy < len(matrix[0]) and matrix[fx][fy]=="#":
        search(matrix, i, plot, (fx, fy))

    fx, fy = newplot[0]+ directions[2][0], newplot[1] + directions[2][1]
    if (fx, fy) in traveled and (plot[0], plot[1], fx, fy) not in cheats:
        diff = traveled[(fx, fy)] - traveled[plot] - i
        if diff >= 50:
            cheats[(plot[0], plot[1], fx, fy)]=diff
            return
    elif fx < len(matrix) and matrix[fx][fy]=="#":
        search(matrix, i,plot, (fx, fy))

    fx, fy = newplot[0]+ directions[3][0], newplot[1] + directions[3][1]
    if (fx, fy) in traveled and (plot[0], plot[1], fx, fy) not in cheats:
        diff = traveled[(fx, fy)] - traveled[plot] - i
        if diff >= 50:
            cheats[(plot[0], plot[1], fx, fy)]=diff
            return
    elif fy > 0 and matrix[fx][fy]=="#":
        search(matrix, i, plot, (fx, fy))

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