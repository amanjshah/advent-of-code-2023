import math
import os


def positionIsInvalid(partNumbers, schematic, idxI, idxJ, seen):
    return (len(partNumbers) > 2
            or idxI >= len(schematic)
            or idxJ >= len(schematic[0])
            or seen[idxI][idxJ]
            or not schematic[idxI][idxJ].isdigit())


def getPartNumber(schematic, seen, idxI, idxJ):
    partNumber, shift, position = '0', 0, schematic[idxI][idxJ]
    while position.isdigit():
        shift -= 1
        position = schematic[idxI][idxJ+shift]
    shift += 1
    position = schematic[idxI][idxJ+shift]
    while position.isdigit():
        partNumber += position
        seen[idxI][idxJ+shift] = True
        shift += 1
        position = schematic[idxI][idxJ+shift]
    return int(partNumber)


def getPartNumbersForSymbol(schematic, seen, i, j):
    partNumbers = []
    for di, dj in ((0, -1), (0, 1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 0), (1, 1)):
        idxI, idxJ = i+di, j+dj
        if positionIsInvalid(partNumbers, schematic, idxI, idxJ, seen):
            continue
        partNumbers.append(getPartNumber(schematic, seen, idxI, idxJ))
    return partNumbers


def getResult():
    schematic = [[char for char in line] for line in open(os.path.join("input-data-2023", "23-3.txt"))]
    return getGearRatioSum(schematic)


def getGearRatioSum(schematic):
    gearRatioSum, seen = 0, [[False for _ in line] for line in schematic]
    for i in range(len(schematic)):
        for j in range(len(schematic[0])):
            if schematic[i][j] == "*":
                partNumbers = getPartNumbersForSymbol(schematic, seen, i, j)
                gearRatioSum += 0 if len(partNumbers) < 2 else math.prod(partNumbers)
    return gearRatioSum


print(getResult())
