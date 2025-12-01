with open("input.txt", 'r') as file:
    total = 50
    zerocount = 0

    for line in file:
        line = line.strip()
        number = int(line[1:])

        if line[0] == "L":

            if total == 0:
                zerocount += number // 100

            elif number >= total:
                zerocount += 1 + (number - total) // 100

            total = (total - number) % 100

        else:  # R
            if total + number >= 100:
                zerocount += (total + number) // 100

            total = (total + number) % 100

    print(zerocount)
