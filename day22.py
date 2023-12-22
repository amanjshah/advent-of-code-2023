import os
from collections import deque
from random import randint


def quicksort(data):
    # If the input contains fewer than two elements, then return it as the result of the function
    if len(data) < 2:
        return data

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    ((_, _, z1), (_, _, z2)) = data[randint(0, len(data) - 1)]
    pivot = min(z1, z2)

    for item in data:
        ((_, _, z1), (_, _, z2)) = item
        # Elements that are smaller than the `pivot` go to the `low` list.
        # Elements that are larger than `pivot` go to the `high` list.
        # Elements that are equal to `pivot` go to the `same` list.
        comparableElement = min(z1, z2)
        if comparableElement < pivot:
            low.append(item)
        elif comparableElement == pivot:
            same.append(item)
        elif comparableElement > pivot:
            high.append(item)

    # The final result combines the sorted `low` list with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)


def getOrderedData():
    data = [line.split("~") for line in open(os.path.join("input-data-2023", "23-22.txt")).read().strip().split("\n")]
    return quicksort([[list(map(int, start.split(","))), list(map(int, end.split(",")))] for start, end in data])


def zPlaneIntersection(a, b):
    (x11, y11, _), (x12, y12, _) = a
    (x21, y21, _), (x22, y22, _) = b
    return max(x11, x21) <= min(x12, x22) and max(y11, y21) <= min(y12, y22)


def simulateFall(data):
    for i, brick in enumerate(data):
        levelToFall = 1
        for lowerBrick in data[:i]:
            lowerBrickLevel = lowerBrick[1][2]
            if levelToFall <= lowerBrickLevel and zPlaneIntersection(brick, lowerBrick):
                levelToFall = lowerBrickLevel + 1
        zDifference = brick[1][2] - brick[0][2]
        brick[0][2] = levelToFall
        brick[1][2] = levelToFall + zDifference
    return data


def getSupportingBricks(data):
    supportedBy = [set() for _ in range(len(data))]
    supporting = [set() for _ in range(len(data))]
    for i in range(len(data)):
        for j in range(i):
            brick, lowerBrick = data[i], data[j]
            if zPlaneIntersection(lowerBrick, brick) and brick[0][2] == lowerBrick[1][2] + 1:
                supportedBy[j].add(i)
                supporting[i].add(j)
    return supportedBy, supporting


def findUnsupportedBricks(brick, queue, falling, supporting, supportedBy):
    for supportedBrick in supportedBy[brick]:
        if supportedBrick not in falling:
            for supportingBrick in supporting[supportedBrick]:
                if supportingBrick not in falling:
                    break
            else:
                queue.append(supportedBrick)
                falling.add(supportedBrick)


def simulateDisintegration(brick, supportedBy, supporting):
    fallen = [supportedBrick for supportedBrick in supportedBy[brick] if len(supporting[supportedBrick]) == 1]
    queue, falling = deque(fallen), set(fallen)
    while queue:
        brick = queue.popleft()
        findUnsupportedBricks(brick, queue, falling, supporting, supportedBy)
    return len(falling)


def getResult():
    data = simulateFall(getOrderedData())
    supportedBy, supporting = getSupportingBricks(data)
    return sum(map(lambda brick: simulateDisintegration(brick, supportedBy, supporting), range(len(data))))


print(getResult())
