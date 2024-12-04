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
            if matrix[i][ii]!='X':
                continue
            total_match += check_horizontal_match(matrix, i, ii, num_columns)
            total_match += check_vertical_match(matrix, i, ii, num_rows)
            total_match += check_diagonal_match(matrix, i, ii, num_rows, num_columns)

    print(f'Total found is {total_match}')

def check_horizontal_match(matrix, row_index, column_index, num_columns):
    num_valid = 0
    # Check horizontal right
    if column_index + 3 < num_columns:
        coordinates_to_check=[[row_index,column_index+1],[row_index,column_index+2],[row_index,column_index+3]]
        if is_valid(coordinates_to_check, matrix):
            num_valid+=1
    
    # Check horizontal left
    if column_index - 3 >= 0:
        coordinates_to_check=[[row_index,column_index-1],[row_index,column_index-2],[row_index,column_index-3]]
        if is_valid(coordinates_to_check, matrix):
            num_valid+=1

    return num_valid

def check_vertical_match(matrix, row_index, column_index, num_rows):
    num_valid = 0
    # Check vertical down
    if row_index + 3 < num_rows:
        coordinates_to_check=[[row_index+1,column_index],[row_index+2,column_index],[row_index+3,column_index]]
        if is_valid(coordinates_to_check, matrix):
            num_valid+=1
    
    # Check vertical up
    if row_index - 3 >= 0:
        coordinates_to_check=[[row_index-1,column_index],[row_index-2,column_index],[row_index-3,column_index]]
        if is_valid(coordinates_to_check, matrix):
            num_valid+=1

    return num_valid

def check_diagonal_match(matrix, row_index, column_index, num_rows, num_columns):
    num_valid = 0
    # Check left up
    if row_index - 3 >= 0 and column_index - 3 >= 0:
        coordinates_to_check=[[row_index-1,column_index-1],[row_index-2,column_index-2],[row_index-3,column_index-3]]
        if is_valid(coordinates_to_check, matrix):
            num_valid+=1
    
    # Check right up
    if row_index - 3 >= 0 and column_index + 3 < num_columns:
        coordinates_to_check=[[row_index-1,column_index+1],[row_index-2,column_index+2],[row_index-3,column_index+3]]
        if is_valid(coordinates_to_check, matrix):
            num_valid+=1

    # Check left down
    if row_index + 3 < num_rows and column_index - 3 >= 0:
        coordinates_to_check=[[row_index+1,column_index-1],[row_index+2,column_index-2],[row_index+3,column_index-3]]
        if is_valid(coordinates_to_check, matrix):
            num_valid+=1

    # Check right down
    if row_index + 3 < num_rows and column_index + 3 < num_columns:
        coordinates_to_check=[[row_index+1,column_index+1],[row_index+2,column_index+2],[row_index+3,column_index+3]]
        if is_valid(coordinates_to_check, matrix):
            num_valid+=1

    return num_valid

def is_valid(coordinates_to_check, matrix):
    if matrix[coordinates_to_check[0][0]][coordinates_to_check[0][1]] == 'M' and \
        matrix[coordinates_to_check[1][0]][coordinates_to_check[1][1]] == 'A' and \
        matrix[coordinates_to_check[2][0]][coordinates_to_check[2][1]] == 'S':
        return True
    return False

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")
