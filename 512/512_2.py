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

    sum_invalid=0
    invalid_updates=[]
    for update in updates:
        i = 0
        while i < len(update):
            if i > 0 and (update[i-1], update[i]) not in order_pairs:
                invalid_updates.append(update)
                break
            i += 1

    for invalid_update in invalid_updates:
        i = 0
        while i < len(invalid_update):
            pairs = ([(invalid_update[i], other) for index, other in enumerate(invalid_update) if i != index])
            if sum(1 for pair in pairs if pair in order_pairs) == (len(invalid_update) // 2):
                sum_invalid+=invalid_update[i]
                break
            i+=1

    print(sum_invalid)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")
