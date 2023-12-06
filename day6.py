import os
import math


def getValues():
    day6 = open(os.path.join("input-data-2023", "23-6.txt")).read().strip().split("\n")
    return (int(''.join(char for char in day6[i] if char.isdigit())) for i in range(2))


def getResult():
    time, distanceToBeat = getValues()
    discriminantSqrt = (time**2-4*distanceToBeat)**0.5
    return math.ceil((time+discriminantSqrt)/2) - math.ceil((time-discriminantSqrt)/2)


print(getResult())
