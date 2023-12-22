import os

data = open(os.path.join("input-data-2023", "23-21.txt")).read().strip().split("\n")
gridLength = len(data)


def plotsAfterSteps(rowStart, colStart, steps):
    plots = {(rowStart, colStart)}
    finalPlots = set()
    for iteration in range(steps):
        plots, finalPlots = plotsAfterStep(iteration, plots, finalPlots, steps)
    finalPlots = finalPlots | set(plots)
    return len(finalPlots)


def plotsAfterStep(iteration, positions, finalPlots, steps):
    newPlots = set()
    for _ in range(len(positions)):
        i, j = positions.pop()
        if iteration % 2 == steps % 2:
            finalPlots.add((i, j))
        addNextPlots(finalPlots, i, j, newPlots)
    return newPlots, finalPlots


def addNextPlots(finalPlots, i, j, newPlots):
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nextI, nextJ = i + di, j + dj
        if (0 <= nextI < gridLength and 0 <= nextJ < gridLength
                and data[nextI][nextJ] != "#" and (nextI, nextJ) not in finalPlots):
            newPlots.add((nextI, nextJ))


def getResult():
    iStart, jStart = [(i, j) for j in range(gridLength) for i in range(gridLength) if data[i][j] == "S"][0]
    totalSteps, dummyEvenSteps = 26501365, gridLength if not gridLength % 2 else gridLength + 1
    maxFullGridsInPath = (totalSteps // gridLength) - 1
    gridsWithOddSteps = (maxFullGridsInPath if maxFullGridsInPath % 2 else maxFullGridsInPath + 1) ** 2
    gridsWithEvenSteps = (maxFullGridsInPath + 1 if maxFullGridsInPath % 2 else maxFullGridsInPath) ** 2
    cornerPlotArgs = ((gridLength - 1, jStart), (0, jStart), (iStart, gridLength - 1), (iStart, 0))
    remainingArgs = ((gridLength - 1, 0), (gridLength - 1, gridLength - 1), (0, gridLength - 1), (0, 0))
    return ((gridsWithOddSteps * plotsAfterSteps(iStart, jStart, dummyEvenSteps + 1))
            + (gridsWithEvenSteps * plotsAfterSteps(iStart, jStart, dummyEvenSteps))
            + sum((plotsAfterSteps(rowStart, colStart, gridLength - 1) for rowStart, colStart in cornerPlotArgs))
            + sum((plotsAfterSteps(rowStart, colStart, gridLength // 2 - 1)
                   for rowStart, colStart in remainingArgs)) * (maxFullGridsInPath + 1)
            + sum((plotsAfterSteps(rowStart, colStart, gridLength * 3 // 2 - 1)
                   for rowStart, colStart in remainingArgs)) * maxFullGridsInPath)


print(getResult())
