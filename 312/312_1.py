import re
import os

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "312_input.txt"

    with open(file_path, "r") as file:
        content = file.read()

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, content)

    total=0
    for num1, num2 in matches:
        total+=(int(num1)*int(num2))

    print(f"Total: {total}")

if __name__ == "__main__":
    main()
