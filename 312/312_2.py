import re
import os

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "312_input.txt"

    with open(file_path, "r") as file:
        content = file.read()

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.finditer(pattern, content)

    valid_matches = []
    for match in matches:
        mul_start = match.start()  
        preceding_text = content[:mul_start]

        last_dont = preceding_text.rfind("don't()")
        last_do = preceding_text.rfind("do()")

        if last_dont == -1 or (last_do > last_dont):
            valid_matches.append(match.groups())

    total=0
    for num1, num2 in valid_matches:
        print(f'Num1 is {num1} and Num2 is {num2}')
        total+=(int(num1)*int(num2))

    print(f"Total: {total}")

if __name__ == "__main__":
    main()
