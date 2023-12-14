import os

data = [list(row) for row in open(os.path.join("input-data-2023", "23-14.txt")).read().strip().split("\n")]
roundedRocks = dict((col, [False for _ in range(len(data[0]))]) for col in range(len(data[0])))
cubedRocks = dict((col, [False for _ in range(len(data[0]))]) for col in range(len(data[0])))

def rotate(data):
    rotatedData = [['X' for _ in range(len(data))] for _ in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            rotatedData[j][len(data) - i - 1] = data[i][j]
    return rotatedData


def pushUp(data):
    load = 0
    for j in range(len(data[0])):
        if data[0][j] == "O":
            load += len(data)
        for i in range(1, len(data)):
            if data[i][j] != "O":
                continue
            pointer = i - 1
            while pointer >= 0 and data[pointer][j] == ".":
                pointer -= 1
            pointer += 1
            data[i][j] = "."
            data[pointer][j] = "O"
            load += len(data) - pointer
    return load, data


print(pushUp(data))
