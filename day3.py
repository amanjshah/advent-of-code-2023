import math
import os

day3 = open(os.path.join("input-data-2023", "23-3.txt"))


def positionIsInvalid(partNumbers, schematic, idxI, idxJ, seen):
    return len(partNumbers)>2 or idxI >= len(schematic) or idxJ >= len(schematic[0]) or seen[idxI][idxJ] or not schematic[idxI][idxJ].isdigit()


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
    return partNumber


def getPartNumbersForSymbol(deltas, schematic, seen, i, j):
    partNumbers = []
    for di,dj in deltas:
        idxI, idxJ = i+di, j+dj
        if positionIsInvalid(partNumbers, schematic, idxI, idxJ, seen): continue
        partNumber = getPartNumber(schematic, seen, idxI, idxJ)
        partNumbers.append(int(partNumber))
    return partNumbers


def getResult(day3):
    gearRatioSum = 0
    deltas = ((0,-1), (0,1), (-1,0), (-1,-1), (-1,1), (1,-1), (1,0), (1,1))
    schematic = [[char for char in line] for line in day3]
    seen = [[False for _ in line] for line in schematic]
    for i in range(len(schematic)):
        for j in range(len(schematic[0])):
            if schematic[i][j] == "*":
                partNumbers = getPartNumbersForSymbol(deltas, schematic, seen, i, j)
                gearRatioSum += 0 if len(partNumbers) != 2 else math.prod(partNumbers)
    return gearRatioSum


print(getResult(day3))