import os


def getData():
    return open(os.path.join("input-data-2023", "23-11.txt")).read().strip().split("\n")


def findGalaxiesAndSpace(data):
    galaxyPositions, emptyRows, emptyColumns = [], [], [True for _ in range(len(data[0]))]
    for row in range(len(data)):
        updateData(data, emptyColumns, emptyRows, galaxyPositions, row)
    return galaxyPositions, emptyRows, [i for i in range(len(emptyColumns)) if emptyColumns[i]]


def updateData(data, emptyColumns, emptyRows, galaxyPositions, row):
    numberOfGalaxies = len(galaxyPositions)
    for col in range(len(data)):
        if data[row][col] == "#":
            galaxyPositions.append((row, col))
            emptyColumns[col] = False
    if numberOfGalaxies == len(galaxyPositions):
        emptyRows.append(row)


def updateGalaxyPositions(dataSize, galaxyPositions, emptyRows, emptyColumns):
    rowAddition, columnAddition = [0 for _ in range(dataSize)], [0 for _ in range(dataSize)]
    for row in emptyRows:
        for i in range(row + 1, dataSize):
            rowAddition[i] += 999999
    for col in emptyColumns:
        for i in range(col + 1, dataSize):
            columnAddition[i] += 999999
    return [(i + rowAddition[i], j + columnAddition[j]) for (i, j) in galaxyPositions]


def getSumOfPaths(galaxyPositions):
    res, seen = 0, set()
    for i1, j1 in galaxyPositions:
        for i2, j2 in galaxyPositions:
            if (i1 == i2 and j1 == j2) or (i2, j2) in seen:
                continue
            res += abs(i2 - i1) + abs(j2 - j1)
        seen.add((i1, j1))
    return res


def getResult():
    day11 = getData()
    initialGalaxyPositions, emptyRows, emptyColumns = findGalaxiesAndSpace(day11)
    galaxyPositions = updateGalaxyPositions(len(day11), initialGalaxyPositions, emptyRows, emptyColumns)
    return getSumOfPaths(galaxyPositions)


print(getResult())
