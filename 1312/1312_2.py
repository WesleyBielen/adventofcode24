import os
import time
import copy

regions = dict()
number_digits_matrix_row = 0
number_digits_matrix_col = 0

def main():
    global number_digits_matrix_col, number_digits_matrix_row
    os.chdir(os.path.dirname(__file__))
    file_path = "1312_input_sample.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    matrix = [list(line.strip()) for line in content]

    number_digits_matrix_row = len(str(len(matrix) - 1))
    number_digits_matrix_col = len(str(len(matrix[0]) - 1))

    for i in range(len(matrix)):
        for ii in range(len(matrix[0])):
            region_id = register_new_region(matrix[i][ii], [i, ii])
            if not region_id is None:
                search_for_region(region_id, matrix[i][ii], matrix, [i, ii])

    total_price = 0
    for region_id, region_list in regions.items():
        sorted_region_list = sorted(region_list, key=lambda x: (x[0], x[1]))
        fences_north = []
        fences_east = []
        fences_south = []
        fences_west = []
        plant_type = None
        total_fences=0
        for plot in sorted_region_list:
            if plant_type is None:
                plant_type=matrix[plot[0]][plot[1]]
            validate_north = False
            if plot[0] > 0:
                pl_to_check = plot[:]
                pl_to_check[0] -= 1
                if not matrix[pl_to_check[0]][pl_to_check[1]] == plant_type:
                    validate_north = True
            else:
                validate_north = True
            if validate_north:
                fences_north.append(plot)

            validate_east = False
            if plot[1] < len(matrix[0])-1:
                pl_to_check = plot[:]
                pl_to_check[1] += 1
                if not matrix[pl_to_check[0]][pl_to_check[1]] == plant_type:
                    validate_east = True
            else:
                validate_east = True
            if validate_east:
                fences_east.append(plot)

            validate_south = False
            if plot[0] < len(matrix) - 1:
                pl_to_check = plot[:]
                pl_to_check[0] += 1
                if not matrix[pl_to_check[0]][pl_to_check[1]] == plant_type:
                    validate_south = True
            else:
                validate_south = True
            if validate_south:
                fences_south.append(plot)

            validate_west = False
            if plot[1] > 0:
                pl_to_check = plot[:]
                pl_to_check[1] -= 1
                if not matrix[pl_to_check[0]][pl_to_check[1]] == plant_type:
                    validate_west = True
            else:
                validate_west = True
            if validate_west:
               fences_west.append(plot)


        for plot in sorted_region_list:
            if plant_type is None:
                plant_type = matrix[plot[0]][plot[1]]
            validate_north = False
            if plot[0] > 0:
                pl_to_check = plot[:]
                pl_to_check[0] -= 1
                if not matrix[pl_to_check[0]][pl_to_check[1]] == plant_type:
                    validate_north = True
            else:
                validate_north = True
            if validate_north:
                if not [plot[0],plot[1]-1] in fences_north:
                    total_fences+=1

            validate_east = False
            if plot[1] < len(matrix[0]) - 1:
                pl_to_check = plot[:]
                pl_to_check[1] += 1
                if not matrix[pl_to_check[0]][pl_to_check[1]] == plant_type:
                    validate_east = True
            else:
                validate_east = True
            if validate_east:
                if not [plot[0]-1,plot[1]] in fences_east:
                    total_fences += 1

            validate_south = False
            if plot[0] < len(matrix) - 1:
                pl_to_check = plot[:]
                pl_to_check[0] += 1
                if not matrix[pl_to_check[0]][pl_to_check[1]] == plant_type:
                    validate_south = True
            else:
                validate_south = True
            if validate_south:
                if not [plot[0],plot[1] - 1] in fences_south:
                    total_fences += 1

            validate_west = False
            if plot[1] > 0:
                pl_to_check = plot[:]
                pl_to_check[1] -= 1
                if not matrix[pl_to_check[0]][pl_to_check[1]] == plant_type:
                    validate_west = True
            else:
                validate_west = True
            if validate_west:
                if not [plot[0]-1,plot[1]] in fences_west:
                    total_fences += 1

        amount_plots = len(sorted_region_list)
        print(f'Region {region_id} has  {amount_plots} * {total_fences}')
        total_price += (total_fences * len(sorted_region_list))

    print(f'Total price is {total_price}')


def is_plot_registered_for_region(curr_pos, region_list):
    return curr_pos in region_list


def is_pos_already_registered(curr_pos):
    return any(curr_pos in value_list for value_list in regions.values())


def register_new_plot_to_region(region_id, pos):
    if not is_pos_already_registered(pos):
        regions[region_id].append(pos)
        return True
    return False


def register_new_region(plant, curr_pos):
    if not is_pos_already_registered(curr_pos):
        unique_region_name = plant + str(curr_pos[0]).zfill(number_digits_matrix_row) + str(curr_pos[1]).zfill(
            number_digits_matrix_col)
        regions[unique_region_name] = [curr_pos]
        return unique_region_name
    return None


def search_for_region(region_id, plant, matrix, curr_pos):
    if curr_pos[0] > 0:
        new_pos = copy.deepcopy(curr_pos)
        new_pos[0] -= 1
        if matrix[new_pos[0]][new_pos[1]] == plant:
            if register_new_plot_to_region(region_id, new_pos):
                search_for_region(region_id, plant, matrix, new_pos)

    if curr_pos[0] < len(matrix) - 1:
        new_pos = copy.deepcopy(curr_pos)
        new_pos[0] += 1
        if matrix[new_pos[0]][new_pos[1]] == plant:
            if register_new_plot_to_region(region_id, new_pos):
                search_for_region(region_id, plant, matrix, new_pos)

    if curr_pos[1] > 0:
        new_pos = copy.deepcopy(curr_pos)
        new_pos[1] -= 1
        if matrix[new_pos[0]][new_pos[1]] == plant:
            if register_new_plot_to_region(region_id, new_pos):
                search_for_region(region_id, plant, matrix, new_pos)

    if curr_pos[1] < len(matrix[0]) - 1:
        new_pos = copy.deepcopy(curr_pos)
        new_pos[1] += 1
        if matrix[new_pos[0]][new_pos[1]] == plant:
            if register_new_plot_to_region(region_id, new_pos):
                search_for_region(region_id, plant, matrix, new_pos)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")