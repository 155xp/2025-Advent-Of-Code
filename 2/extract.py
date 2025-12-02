# extracts each individual number from input.txt
with open("input.txt") as f:
    line = f.read().strip()


with open("numbers.txt", "w") as out:
    for part in line.split(","):
        if "-" in part:
            a, b = map(int, part.split("-"))
            start, end = min(a,b), max(a,b)

            for i in range(start, end + 1):
                out.write(str(i) + "\n")