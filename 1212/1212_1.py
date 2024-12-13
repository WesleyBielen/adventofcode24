import os
import time
import copy

regions= dict()
number_digits_matrix_row=0
number_digits_matrix_col=0
def main():
    global number_digits_matrix_col, number_digits_matrix_row
    os.chdir(os.path.dirname(__file__))
    file_path = "1212_input_sample.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    matrix = [list(line.strip()) for line in content]

    number_digits_matrix_row = len(str(len(matrix)-1))
    number_digits_matrix_col = len(str(len(matrix[0])-1))
    
    for i in range(len(matrix)):
        for ii in range(len(matrix[0])):
            region_id = register_new_region(matrix[i][ii], [i,ii])
            if not region_id is None:
                search_for_region(region_id,matrix[i][ii], matrix, [i,ii])

    print(regions.values())

def is_pos_already_registered(curr_pos):
    return any(curr_pos in value for value in regions.values())

def register_new_plot_to_region(region_id, pos):
    if not is_pos_already_registered(pos):
        regions[region_id].append(pos)
        return True
    return False

def register_new_region(plant, curr_pos):
    if not is_pos_already_registered(curr_pos):
        unique_region_name = plant + str(curr_pos[0]).zfill(number_digits_matrix_row) + str(curr_pos[1]).zfill(number_digits_matrix_col)
        regions[unique_region_name] = [curr_pos]
        return unique_region_name
    return None

def search_for_region(region_id,plant, matrix, curr_pos):
    new_pos = copy.deepcopy(curr_pos)

    row = new_pos[0]
    col = new_pos[1]
    if row > 0:
        row-=1
        new_pos[0] = row 
        if matrix[new_pos[0]][new_pos[1]] == plant:
            if register_new_plot_to_region(region_id, new_pos):
                search_for_region(region_id, plant, matrix, new_pos)
    
    if row < len(matrix)-1:
        row+=1
        new_pos[0] = row 
        if matrix[new_pos[0]][new_pos[1]] == plant:
            if register_new_plot_to_region(region_id, new_pos):
                search_for_region(region_id, plant, matrix, new_pos)
    
    if col > 0:
        col-=1
        new_pos[1] = col
        if matrix[new_pos[0]][new_pos[1]] == plant:
            if register_new_plot_to_region(region_id, new_pos):
                search_for_region(region_id, plant, matrix, new_pos)
    
    if col < len(matrix[0])-1:
        col+=1
        new_pos[1] = col
        if matrix[new_pos[0]][new_pos[1]] == plant:
            if register_new_plot_to_region(region_id, new_pos):
                search_for_region(region_id, plant, matrix, new_pos)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")