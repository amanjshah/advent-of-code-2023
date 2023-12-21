import os


def plotsAfterSteps(iStart, jStart, steps):
    plots = {(iStart, jStart)}
    finalPlots = set()
    for iteration in range(steps):
        plots, finalPlots = plotsAfterStep(iteration, plots, finalPlots, steps)
    finalPlots = finalPlots | set(plots)
    return finalPlots


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
        if (0 <= nextI < len(data) and 0 <= nextJ < len(data[0])
                and data[nextI][nextJ] != "#" and (nextI, nextJ) not in finalPlots):
            newPlots.add((nextI, nextJ))


data = open(os.path.join("input-data-2023", "23-21.txt")).read().strip().split("\n")
iStart, jStart = [(i, j) for j in range(len(data[0])) for i in range(len(data)) if data[i][j] == "S"][0]
res = len(plotsAfterSteps(iStart, jStart, 64))
print(res)
