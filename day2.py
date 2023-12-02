import math
import os

day2 = open(os.path.join("input-data-2023", "23-2.txt"))

def getResult(dayTwoFile):
    return sum(getPowerOfSet(line) for line in dayTwoFile)

def getPowerOfSet(line):
    game = line.split(":")[1].strip().split("; ")
    minimumNumbers = {"red": 0, "green": 0, "blue": 0}
    for gameSet in game: adjustMinimumNumbersForSet(minimumNumbers, gameSet)
    return math.prod(minimumNumbers.values())

def adjustMinimumNumbersForSet(minimumNumbers, gameSet):
    colourNumbers = gameSet.split(",")
    for unknownColour in colourNumbers:
        number, colour = unknownColour.split()
        minimumNumbers[colour] = max(int(number), minimumNumbers[colour])

res = getResult(day2)

print(res)