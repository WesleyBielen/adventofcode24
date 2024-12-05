import os
import time

def main():
    os.chdir(os.path.dirname(__file__))
    file_path_orderings = "512_input_orderings.txt"
    file_path_updates = "512_input_updates.txt"

    with open(file_path_orderings, "r") as file:
        content = file.read()

    with open(file_path_updates, "r") as file:
        content_updates = file.read()
    order_pairs = [tuple(map(int, line.split('|'))) for line in content.splitlines()]

    updates = [list(map(int, line.split(','))) for line in content_updates.splitlines()]

    #print(order_pairs)
    total_valid = 0
    sum_valid=0
    for update in updates:
        i = 0
        valid = True
        while i < len(update):
            if i > 0 and (update[i-1], update[i]) not in order_pairs:
                valid = False
                break
            i += 1
        if valid:
            total_valid+=1
            sum_valid+=update[(len(update) // 2)]

    print(total_valid)
    print(sum_valid)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")
