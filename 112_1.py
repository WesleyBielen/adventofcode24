

def main():
    file_path = "112_input.txt"

    list1 = []
    list2 = []

    with open(file_path, "r") as file:
        for line in file:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)

    list1 = sorted(list1)
    list2 = sorted(list2)

    total=0
    for i in range(len(list1)):
        total+=abs(list1[i] - list2[i])

    print(f"Total: {total}")

if __name__ == "__main__":
    main()
