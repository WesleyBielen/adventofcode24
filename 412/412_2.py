import os
import time

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "412_input.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    matrix = [list(line.strip()) for line in content]

    num_rows = len(matrix)             
    num_columns = len(matrix[0])

    total_match = 0
    for i in range(num_rows):
        for ii in range(num_columns):
            if matrix[i][ii]!='A':
                continue
            total_match += check_match_for_x(matrix, i, ii, num_rows, num_columns)

    print(f'Total found is {total_match}')

def check_match_for_x(matrix, row_index, column_index, num_rows, num_columns):
    num_valid = 0
    
    if row_index - 1 >= 0 and row_index + 1 < num_rows and column_index - 1 >= 0 and column_index + 1 < num_columns:
        coordinates_to_check=[[row_index-1,column_index-1],[row_index+1,column_index+1],[row_index-1,column_index+1],[row_index+1,column_index-1]]
        if is_valid(coordinates_to_check, matrix):
            num_valid+=1
    
    return num_valid

def is_valid(coordinates_to_check, matrix):
    left_up = matrix[coordinates_to_check[0][0]][coordinates_to_check[0][1]]
    right_down = matrix[coordinates_to_check[1][0]][coordinates_to_check[2][1]]
    right_up = matrix[coordinates_to_check[2][0]][coordinates_to_check[2][1]]
    left_down = matrix[coordinates_to_check[3][0]][coordinates_to_check[3][1]]
    if ((left_up == 'M' and right_down == 'S') or (left_up == 'S' and right_down == 'M')) and \
       ((right_up== 'M' and left_down == 'S') or (right_up == 'S' and left_down == 'M')):
        return True
    return False

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")
