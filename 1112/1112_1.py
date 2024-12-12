import os
import time
import copy


def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "1112_input.txt"

    with open(file_path, "r") as file:
        content = file.read()

    list = content.split()
    ctr = dict()
    ctr = {i: ctr.get(i, 0) + 1 for i in list}
    print(f'INitial ctr = {ctr}')
    for i in range(500):
        old_ctr = copy.deepcopy(ctr)
        ctr=dict()
        for k, value in old_ctr.items():
            key = int(k)
            if key == 0:
                update_dict(ctr, 1, value)
                continue

            digits = len(str(key))
            if digits % 2 == 0:
                left_num = int(str(key)[:digits//2])
                update_dict(ctr, left_num, value)
                right_num = int(str(key)[digits//2:])
                update_dict(ctr, right_num, value)
                continue
            
            multipl = int(key) * 2024
            update_dict(ctr, multipl, value)
           
    print(f'Total = {sum(ctr.values())}')

def update_dict(ctr, key, value):
    if key in ctr:
        ctr[key] = ctr[key]+value
    else:
        ctr[key] = value

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")