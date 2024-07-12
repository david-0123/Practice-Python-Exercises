prime = []
happy = []

with open("prime.txt", "r") as p:
    line = p.readline()
    while line:
        prime.append(int(line))
        line = p.readline()

with open("happy.txt", "r") as h:
    line = h.readline()
    while line:
        happy.append(int(line))
        line = h.readline()

print(list(set(prime) & set(happy)))