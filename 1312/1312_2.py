import os
import time
import re
from sympy import symbols, Eq, solve

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "1312_input.txt"

    with open(file_path, "r") as file:
        content = file.readlines()

    matrix = [line.strip() for line in content]

    button_a = None
    button_b = None
    price = None
    total_price=0
    for i in range(len(matrix)):
        line = matrix[i]
        modus = i % 4
        if modus == 0:
            button_a = []
            pattern = r"X\+(\d+)"
            match = re.search(pattern, line)
            button_a.append(match.group(1))
            pattern = r"Y\+(\d+)"
            match = re.search(pattern, line)
            button_a.append(match.group(1))
        elif modus ==1:
            button_b = []
            pattern = r"X\+(\d+)"
            match = re.search(pattern, line)
            button_b.append(match.group(1))
            pattern = r"Y\+(\d+)"
            match = re.search(pattern, line)
            button_b.append(match.group(1))
        elif modus == 2:
            price = []
            pattern = r"X\=(\d+)"
            match = re.search(pattern, line)
            price.append("1"+match.group(1).zfill(13))
            pattern = r"Y\=(\d+)"
            match = re.search(pattern, line)
            price.append("1"+match.group(1).zfill(13))

            x, y = symbols('x y', integer=True)

            eq1 = Eq(int(button_a[0]) * x + int(button_b[0]) * y, int(price[0]))
            eq2 = Eq(int(button_a[1]) * x + int(button_b[1]) * y, int(price[1]))

            solution = solve((eq1, eq2), (x, y))
            if solution:
                total_price += solution[x] * 3 + solution[y]
    print(f"Total tokens = {total_price}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program completed in {elapsed_time:.5f} seconds")