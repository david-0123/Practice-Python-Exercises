names = {}

with open("names.txt", "r") as f:
    line = f.readline().strip()
    while line:
        if line not in names:
            names[line] = 1
        else:
            names[line] += 1
        line = f.readline().strip()

print(names)