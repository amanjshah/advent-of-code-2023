import os

data, validSymbols = open(os.path.join("input-data-2023", "23-23.txt")).read().strip().split("\n"), ".v<>^"


def validateCoordinates(i, j, cache):
    return 0 <= i < len(data) and 0 <= j < len(data[0]) and (i, j) not in cache and data[i][j] in validSymbols


def getBranches():
    branches = set(sum(validateCoordinates(i + di, j + dj, set()) for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]) > 2
                   and (i, j) for j in range(len(data[0])) for i in range(len(data)))
    branches.remove(False)
    return branches


def createGraph(branches):
    graph = {branch: {} for branch in branches}
    for branch in branches:
        addBranchToGraph(branch, branches, graph)
    return graph


def addBranchToGraph(branch, branches, graph):
    stack, cache = [(branch[0], branch[1], 0)], {branch}
    while stack:
        i, j, steps = stack.pop()
        if steps and (i, j) in branches:
            graph[branch][(i, j)] = steps
            continue
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nextI, nextJ = i + di, j + dj
            if validateCoordinates(nextI, nextJ, cache):
                stack.append((nextI, nextJ, steps + 1))
                cache.add((nextI, nextJ))


def findLongestPath(graph, start, end):
    stack, res = [(start[0], start[1], 0, {start})], -1
    while stack:
        i, j, steps, cache = stack.pop()
        if (i, j) == end:
            res = max(res, steps)
        for nextI, nextJ in graph[(i, j)]:
            if (nextI, nextJ) not in cache:
                stack.append((nextI, nextJ, steps + graph[(i, j)][(nextI, nextJ)], cache | {(nextI, nextJ)}))
    return res


def getResult():
    start, end = (0, data[0].find(".")), (len(data) - 1, data[-1].find("."))
    graph = createGraph(getBranches() | {start, end})
    res = findLongestPath(graph, start, end)
    return res


print(getResult())
