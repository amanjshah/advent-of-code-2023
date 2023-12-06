import os


def getValues():
    day6 = open(os.path.join("input-data-2023", "23-6.txt")).read().strip().split("\n")
    return (int(''.join(char for char in day6[i] if char.isdigit())) for i in range(2))


def firstBeatingButtonDuration(time, distanceToBeat):
    # binary search
    left, right = 1, time-1
    while left < right:
        speed = left + (right - left) // 2
        if distanceToBeat < speed*(time-speed):
            right = speed
        else:
            left = speed + 1
    return left


def getResult():
    time, distanceToBeat = getValues()
    return time - 2*firstBeatingButtonDuration(time, distanceToBeat) + 1


print(getResult())
