
with open("numbers.txt", "r") as file:
    total = 0
    for number in file:
        stripped_num = number.strip() # removes the \n linebreak which previously messed up the len function
        length = len(stripped_num)
        is_invalid = False

        for unit_len in range(1, length // 2 + 1):
            if length % unit_len != 0:
                continue

            
            unit = stripped_num[:unit_len]
            repeat_count = length // unit_len

            if unit * repeat_count == stripped_num:
                is_invalid = True
                break

        if is_invalid:
            total += int(stripped_num)




print(total)