import os

day14 = open(os.path.join("input-data-2023", "23-14.txt")).read().strip().split("\n")
print(day14)
roundedRocks = dict((col, [False for _ in range(len(day14[0]))]) for col in range(len(day14[0])))
cubedRocks = dict((col, [False for _ in range(len(day14[0]))]) for col in range(len(day14[0])))
for i in range(len(day14)):
    for j in range(len(day14[0])):
        if day14[i][j] == "O":
            roundedRocks[j][i] = True
        elif day14[i][j] == "#":
            cubedRocks[j][i] = True
load = 0
for c in range(len(day14[0])):
    if roundedRocks[c][0]:
        load += len(day14)
    for r in range(1, len(day14)):
        if not roundedRocks[c][r]:
            continue
        pointer = r-1
        while not (pointer < 0 or roundedRocks[c][pointer] or cubedRocks[c][pointer]):
            pointer -= 1
        pointer += 1
        roundedRocks[c][r] = False
        roundedRocks[c][pointer] = True
        load += len(day14) - pointer