import os


def getData():
    return [[*line] for line in open(os.path.join("input-data-2023", "23-10.txt")).read().strip().split("\n")]


def getStartingPoint(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "S":
                return i, j


def getDataForTraversal(maze, iStart, jStart):
    deltas, initialPositions = getInitialPositions(iStart, jStart, maze)
    replaceStart(deltas, iStart, jStart, maze)
    return maze, initialPositions


def replaceStart(deltas, iStart, jStart, maze):
    (di1, dj1), (di2, dj2) = deltas
    if di1 == di2:
        maze[iStart][jStart] = "-"
    elif dj1 == dj2:
        maze[iStart][jStart] = "|"
    elif (di1, dj1, di2) == (0, 1, 1) or (di2, dj2, di1) == (0, 1, 1):
        maze[iStart][jStart] = "F"
    elif (di1, dj1, di2) == (0, 1, -1) or (di2, dj2, di1) == (0, 1, -1):
        maze[iStart][jStart] = "L"
    elif (di1, dj1, di2) == (0, -1, 1) or (di2, dj2, di1) == (0, -1, 1):
        maze[iStart][jStart] = "7"
    else:
        maze[iStart][jStart] = "J"
    return maze


def getInitialPositions(iStart, jStart, maze):
    initialPositions, deltas = [], []
    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        newInitialPosition = getInitialPosition(maze[iStart + di][jStart + dj], iStart, jStart, di, dj)
        if newInitialPosition:
            initialPositions.append(newInitialPosition)
            deltas.append((di, dj))
    return deltas, initialPositions


def getInitialPosition(pipe, iStart, jStart, di, dj):
    if dj == 1 and pipe in "J7-":
        return pipe, iStart + di, jStart + dj, "W"
    elif dj == -1 and pipe in "LF-":
        return pipe, iStart + di, jStart + dj, "E"
    elif di == 1 and pipe in "LJ|":
        return pipe, iStart + di, jStart + dj, "N"
    elif di == -1 and pipe in "7F|":
        return pipe, iStart + di, jStart + dj, "S"


def getNextPosition(directionTo, maze, i, j):
    di, dj, opp = {"N": (-1, 0, "S"), "S": (1, 0, "N"), "W": (0, -1, "E"), "E": (0, 1, "W")}[directionTo]
    return maze[i + di][j + dj], i + di, j + dj, opp


def getFurthestNode(currentPoints, maze, seen):
    pipeDirections = {"-": "EW", "|": "NS", "L": "EN", "J": "WN", "F": "ES", "7": "WS"}
    iterations = 0
    while currentPoints:
        iterations += 1
        currentPoints = updateCurrentNodes(currentPoints, maze, pipeDirections, seen)
    return iterations, seen


def updateCurrentNodes(currentPoints, maze, pipeDirections, seen):
    nextPoints = []
    for (pipe, i, j, directionFrom) in currentPoints:
        seen[i][j] = True
        directions = pipeDirections[pipe]
        directionTo = directions[0] if directionFrom == directions[1] else directions[1]
        newPipe, newI, newJ, newDirFrom = getNextPosition(directionTo, maze, i, j)
        if newPipe in pipeDirections and newDirFrom in pipeDirections[newPipe] and not seen[newI][newJ]:
            nextPoints.append((newPipe, newI, newJ, newDirFrom))
    currentPoints = nextPoints
    return currentPoints


def updateCrossCount(pipe, lastNonHorizontal, crossCount):
    if pipe == "-":
        return lastNonHorizontal, crossCount
    if (pipe == "|"
            or (pipe == "7" and lastNonHorizontal == "L")
            or (pipe == "J" and lastNonHorizontal == "F")):
        return pipe, crossCount + 1
    return pipe, crossCount


def getArea(maze, partOfLoop):
    res = 0
    for i in range(len(maze)):
        lastNonHorizontal, crossCount = None, 0
        for j in range(len(maze[0])):
            if partOfLoop[i][j]:
                lastNonHorizontal, crossCount = updateCrossCount(maze[i][j], lastNonHorizontal, crossCount)
            else:
                res += crossCount % 2
    return res


def getResult():
    maze = getData()
    seen, (iStart, jStart) = [[False for _ in line] for line in maze], getStartingPoint(maze)
    seen[iStart][jStart] = True
    maze, initialPositions = getDataForTraversal(maze, iStart, jStart)
    _, seen = getFurthestNode(initialPositions, maze, seen)
    return getArea(maze, seen)


print(getResult())
