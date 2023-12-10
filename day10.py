import os


def getData():
    return [[*line] for line in open(os.path.join("input-data-2023", "23-10.txt")).read().strip().split("\n")]


def getStartingPoint(day10):
    for i in range(len(day10)):
        for j in range(len(day10[0])):
            if day10[i][j] == "S":
                return i, j


def getInitialPositions(day10, iStart, jStart):
    initialPositions = []
    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        pipe = day10[iStart + di][jStart + dj]
        if dj == 1 and pipe in "J7-":
            initialPositions.append((pipe, iStart + di, jStart + dj, "W"))
        elif dj == -1 and pipe in "LF-":
            initialPositions.append((pipe, iStart + di, jStart + dj, "E"))
        elif di == 1 and pipe in "LJ|":
            initialPositions.append((pipe, iStart + di, jStart + dj, "N"))
        elif di == -1 and pipe in "7F|":
            initialPositions.append((pipe, iStart + di, jStart + dj, "S"))
    return initialPositions


def getNextPosition(directionTo, day10, i, j):
    if directionTo == "N":
        return day10[i - 1][j], i - 1, j, "S"
    elif directionTo == "S":
        return day10[i + 1][j], i + 1, j, "N"
    elif directionTo == "W":
        return day10[i][j - 1], i, j - 1, "E"
    else:
        return day10[i][j + 1], i, j + 1, "W"


def getFurthestNode(currentPoints, day10, seen):
    pipeDirections = {"-": "EW", "|": "NS", "L": "EN", "J": "WN", "F": "ES", "7": "WS"}
    iterations = 0
    while currentPoints:
        iterations += 1
        nextPoints = []
        for (pipe, i, j, directionFrom) in currentPoints:
            seen[i][j] = True
            directions = pipeDirections[pipe]
            directionTo = directions[0] if directionFrom == directions[1] else directions[1]
            newPipe, newI, newJ, newDirFrom = getNextPosition(directionTo, day10, i, j)
            if newPipe in pipeDirections and newDirFrom in pipeDirections[newPipe] and not seen[newI][newJ]:
                nextPoints.append((newPipe, newI, newJ, newDirFrom))
        currentPoints = nextPoints
    return iterations, seen


def getResult():
    day10 = getData()
    seen = [[False for _ in line] for line in day10]
    iStart, jStart = getStartingPoint(day10)
    seen[iStart][jStart] = True
    initialPositions = getInitialPositions(day10, iStart, jStart)
    return getFurthestNode(initialPositions, day10, seen)[0]


print(getResult())
