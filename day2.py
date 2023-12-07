import math
import os


def getResult():
    return sum(getPowerOfSet(line) for line in open(os.path.join("input-data-2023", "23-2.txt")))


def getPowerOfSet(line):
    minimumNumbers = {"red": 0, "green": 0, "blue": 0}
    for gameSet in line.split(":")[1].strip().split("; "):
        adjustMinimumNumbersForSet(minimumNumbers, gameSet)
    return math.prod(minimumNumbers.values())


def adjustMinimumNumbersForSet(minimumNumbers, gameSet):
    colourNumbers = gameSet.split(",")
    for unknownColour in colourNumbers:
        number, colour = unknownColour.split()
        minimumNumbers[colour] = max(int(number), minimumNumbers[colour])


print(getResult())
