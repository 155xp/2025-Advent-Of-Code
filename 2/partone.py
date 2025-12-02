with open("numbers.txt", "r") as file:
    total = 0
    for number in file:
        strippednum = number.strip() # removes the \n linebreak which previously messed up the len function
        if len(strippednum) % 2 == 0 and strippednum[:len(strippednum)//2] == strippednum[len(strippednum)//2:]:
            total += int(strippednum)


print(total)