import os

def main():
    os.chdir(os.path.dirname(__file__))
    file_path = "112_input.txt"

    list1 = []
    list2 = []

    with open(file_path, "r") as file:
        for line in file:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)

    total=0
    for item in list1:
        total+= item * list2.count(item)

    print(f"Total: {total}")

if __name__ == "__main__":
    main()
