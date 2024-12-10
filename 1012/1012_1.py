import re
import os
import time

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "1012_input_sample.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    matrix = [list(line.strip()) for line in content]
    trailheads_start_pos = []
    for i in range(len(matrix)):
        for ii in range(len(matrix[i])):
            if matrix[i][ii] == '0':
                trailheads_start_pos.append([i,ii])
    
    for i in range(len(trailheads_start_pos)):
        trailhead_start_pos = trailheads_start_pos[i]
        # Look up 
        if trailhead_start_pos[0] > 0:
            
    print(trailheads_start_pos)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")
