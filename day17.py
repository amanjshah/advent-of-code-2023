import os
from heapq import heappush, heappop, heapify


data = open(os.path.join("input-data-2023", "23-17.txt")).read().strip().split()
coordinates = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}


def goStraight(score, i, j, direction, moves, heap):
    if moves < 10:
        di, dj = coordinates[direction]
        if 0 <= i + di < len(data) and 0 <= j + dj < len(data[0]):
            heappush(heap, (score + int(data[i + di][j + dj]), i + di, j + dj, direction, moves + 1))


def turn(score, i, j, direction, moves, heap):
    if moves >= 4:
        for newDirection in "UD" if direction in "LR" else "LR":
            di, dj = coordinates[newDirection]
            if 0 <= i + di < len(data) and 0 <= j + dj < len(data[0]):
                heappush(heap, (score + int(data[i + di][j + dj]), i + di, j + dj, newDirection, 1))


def getResult():
    heap, seen = [(int(data[0][1]), 0, 1, "R", 1), (int(data[1][0]), 1, 0, "D", 1)], set()
    heapify(heap)

    while heap:
        # heap node schema: (heat loss score thus far, row, col, current direction, no of moves in current direction)
        score, i, j, direction, moves = heappop(heap)

        if i == len(data) - 1 and j == len(data[0]) - 1 and moves >= 4:
            return score

        if (i, j, direction, moves) not in seen:
            seen.add((i, j, direction, moves))
            goStraight(score, i, j, direction, moves, heap)
            turn(score, i, j, direction, moves, heap)

    return -1


print(getResult())
