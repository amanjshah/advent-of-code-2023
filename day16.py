import os
from collections import deque

data = open(os.path.join("input-data-2023", "23-16.txt")).read().strip().split()
coordinates = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}
mirrors = {"/": {"R": "U", "L": "D", "U": "R", "D": "L"},
           "\\": {"R": "D", "L": "U", "U": "L", "D": "R"}}
splitters = {"-": "LR", "|": "UD"}


def getEnergisedTiles(rowStart, colStart, dirStart):
    seen = set()
    queue = deque([(rowStart, colStart, dirStart)])
    while queue:
        for _ in range(len(queue)):
            i, j, direction = queue.popleft()
            if (i, j, direction) not in seen and 0 <= i < len(data) and 0 <= j < len(data[0]):
                seen.add((i, j, direction))
                symbol = data[i][j]
                if symbol == "." or (symbol == "-" and direction in "RL") or (symbol == "|" and direction in "UD"):
                    di, dj = coordinates[direction]
                    queue.append((i + di, j + dj, direction))
                elif symbol in "-|":
                    for newDirection in splitters[symbol]:
                        di, dj = coordinates[newDirection]
                        queue.append((i + di, j + dj, newDirection))
                else:
                    newDirection = mirrors[symbol][direction]
                    di, dj = coordinates[newDirection]
                    queue.append((i + di, j + dj, newDirection))
    return len({(i, j) for (i, j, _) in seen})


def getResult():
    res = 0
    for startingRow in range(len(data)):
        res = max(res, getEnergisedTiles(startingRow, 0, "R"))
        res = max(res, getEnergisedTiles(startingRow, len(data[0]) - 1, "L"))
    for startingColumn in range(len(data)):
        res = max(res, getEnergisedTiles(0, startingColumn, "D"))
        res = max(res, getEnergisedTiles(len(data) - 1, startingColumn, "U"))
    return res


print(getResult())
