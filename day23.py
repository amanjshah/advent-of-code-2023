import os

data = open(os.path.join("input-data-2023", "23-23.txt")).read().strip().split("\n")
start = 0, data[0].find("."), 0, {(0, data[0].find("."))}
end = len(data) - 1, data[-1].find(".")
stack = [start]
maxDistances = [[-1 for _ in range(len(data[0]))] for _ in range(len(data))]

while stack:
    i, j, steps, cache = stack.pop()
    assert(steps == len(cache)-1)
    if steps > maxDistances[i][j]:
        maxDistances[i][j] = steps
        steps = maxDistances[i][j]
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nextI, nextJ = i + di, j + dj
            if 0 <= nextI < len(data) and 0 <= nextJ < len(data[0]) and (nextI, nextJ) not in cache:
                nextSymbol = data[nextI][nextJ]
                if nextSymbol in ".v<>^":
                    stack.append((nextI, nextJ, steps + 1, cache | {(nextI, nextJ)}))
print(maxDistances[end[0]][end[1]])

