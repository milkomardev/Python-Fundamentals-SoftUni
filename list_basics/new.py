inpt_list = [int(x) for x in input().split()]
result_list = inpt_list
while True:
    command_line = input()
    if command_line == "end":
        break
    else:
        command = command_line.split()[0]

        if command == "exchange":
            split_index = int(command_line.split()[1])
            if 0 <= split_index < len(result_list):
                result_list = result_list[split_index + 1:] + result_list[:split_index + 1]
            else:
                print("Invalid index")
                continue
        elif command == "max" or command == "min":
            number = 0
            if command_line.split()[1] == "even":
                if not [x for x in result_list if x % 2 == 0]:
                    print("No matches")
                    continue
                else:
                    if command == "max":
                        number = max([x for x in result_list if x % 2 == 0])
                    elif command == "min":
                        number = min([x for x in result_list if x % 2 == 0])

            elif command_line.split()[1] == "odd":
                if not [x for x in result_list if x % 2 == 1]:
                    print("No matches")
                    continue
                else:
                    if command == "max":
                        number = max([x for x in result_list if x % 2 == 1])
                    elif command == "min":
                        number = min([x for x in result_list if x % 2 == 1])

            if result_list.count(number) > 1:
                for i in range(len(result_list) - 1, -1, -1):
                    if result_list[i] == number:
                        print(i)
                        break
            else:
                print(result_list.index(number))

        # elif command == "first" or command == "last":
        #     count = int(command_line.split()[1])
        #     new_list = []
        #
        #     if count > len(result_list):
        #         print("Invalid count")
        #         continue
        #     else:
        #         if command_line.split()[2] == "even":
        #             new_list = [x for x in result_list if x % 2 == 0]
        #         elif command_line.split()[2] == "odd":
        #             new_list = [x for x in result_list if x % 2 == 1]
        #
        #         if command == "first":
        #             new_list = new_list[:count]
        #             print(new_list)
        #         elif command == "last":
        #             new_list = new_list[len(new_list) - count:]
        #             print(new_list)

print(result_list)
