import os


def rotateClockwise(data):
    rotatedData = [['X' for _ in range(len(data))] for _ in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            rotatedData[j][len(data) - i - 1] = data[i][j]
    return rotatedData


def pushUp(data):
    for j in range(len(data[0])):
        for i in range(1, len(data)):
            if data[i][j] != "O":
                continue
            pointer = i - 1
            while pointer >= 0 and data[pointer][j] == ".":
                pointer -= 1
            pointer += 1
            data[i][j] = "."
            data[pointer][j] = "O"
    return data


def getLoad(data):
    load = 0
    for j in range(len(data[0])):
        for i in range(0, len(data)):
            if data[i][j] == "O":
                load += len(data) - i
    return load


def performCycle(data):
    for _ in range(4):
        data = pushUp(data)
        data = rotateClockwise(data)
    return data


def updateCycleNumber(cache, data, cycle):
    hashableData = tuple(tuple(row) for row in data)
    if hashableData in cache:
        cycleLength = cycle - cache[hashableData]
        numberOfCycles = ((1000000000 - cycle) // cycleLength)
        cycle += numberOfCycles * cycleLength
    cache[hashableData] = cycle
    return cycle


def getResult():
    data = [list(row) for row in open(os.path.join("input-data-2023", "23-14.txt")).read().strip().split("\n")]
    cache = {}
    cycle = 0
    while cycle < 1000000000:
        data = performCycle(data)
        cycle = updateCycleNumber(cache, data, cycle + 1)
    return getLoad(data)


print(getResult())
