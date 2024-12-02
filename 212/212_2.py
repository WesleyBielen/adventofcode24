

def main():
    file_path = "212_input.txt"

    with open(file_path, "r") as file:
        lines = file.readlines()

    result = {index: list(map(int, line.split())) for index, line in enumerate(lines)}

    total_valid=0
    for report_data in result.values():
        sliced_report_data = [report_data[:i] + report_data[i+1:] for i in range(len(report_data))]
        for report_line in sliced_report_data:
            first = True
            decrease = False
            increase = False
            previous_num = 0
            invalid = False
            for report_num in report_line:
                if not first:
                    if not decrease and not increase:
                        if previous_num > report_num:
                            decrease = True
                        elif report_num > previous_num:
                            increase = True
                        else:
                            invalid = True
                            break

                    if abs(report_num - previous_num) < 1 or abs(report_num - previous_num) > 3:
                        invalid = True
                        break

                    if (decrease and report_num > previous_num) or (increase and previous_num > report_num):
                        invalid = True
                        break

                previous_num = report_num
                first = False

            if not invalid:
                total_valid += 1
                break
    print(f'Total valid = {total_valid}')

if __name__ == "__main__":
    main()