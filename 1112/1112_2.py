import os
import time
import copy


def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "1112_input.txt"

    with open(file_path, "r") as file:
        content = file.read()

    list = content.split()
    total_sum=0
    for number in list:
        ctr = dict()
        ctr = {number: 1}
        for i in range(75):
            old_ctr = copy.deepcopy(ctr)
            ctr=dict()
            for key, value in old_ctr.items():
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
            
            #print(f'#Dict after {i} = {ctr}')
        total_sum+=sum(ctr.values())
    print(f'Total = {total_sum}')

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