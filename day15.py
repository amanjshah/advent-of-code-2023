import os


def getBoxNumber(line, setterIdx):
    boxNumber = 0
    for char in line[:setterIdx]:
        boxNumber += ord(char)
        boxNumber *= 17
        boxNumber %= 256
    return boxNumber


def dealWithDash(lenses, line):
    for (code, focalLength) in lenses:
        if code == line[:-1]:
            lenses.remove((code, focalLength))
    return lenses


def dealWithEquals(lenses, line, setterIdx):
    for (i, (code, focalLength)) in enumerate(lenses):
        if code == line[:setterIdx]:
            lenses[i] = (code, int(line[setterIdx + 1:]))
            return lenses
    return lenses + [(line[:setterIdx], int(line[setterIdx + 1:]))]


def calculateFocusingPower(boxes):
    res = 0
    for boxNumber in range(len(boxes)):
        for i, (code, focalLength) in enumerate(boxes[boxNumber]):
            res += (1 + boxNumber) * (1 + i) * focalLength
    return res


def getBoxes():
    boxes = [[] for _ in range(256)]
    for line in open(os.path.join("input-data-2023", "23-15.txt")).read().strip().split(","):
        updateBoxes(boxes, line)
    return boxes


def updateBoxes(boxes, line):
    setterIdx = line.find("=")
    boxNumber = getBoxNumber(line, setterIdx)
    if setterIdx == -1:
        boxes[boxNumber] = dealWithDash(boxes[boxNumber], line)
    else:
        boxes[boxNumber] = dealWithEquals(boxes[boxNumber], line, setterIdx)


def getResult():
    return calculateFocusingPower(getBoxes())


print(getResult())
