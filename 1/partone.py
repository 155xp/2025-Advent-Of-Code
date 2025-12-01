with open("input.txt", 'r') as file:
    total = 50

    zerocount = 0

    for line in file:
        number = int(line[1: ])
        
        if line[0] == "L":
            total = (total - number) % 100
        elif line[0] == "R":
            total = (total + number) % 100

        if total == 0:
            zerocount += 1

    print(zerocount)

