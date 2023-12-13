import os


def checkForSmudge(foundSmudge, leftRow, rightRow):
    if (not foundSmudge) and (sum(a != b for a, b in zip(leftRow, rightRow)) == 1):
        leftRow = rightRow
        foundSmudge = True
    return foundSmudge, leftRow, rightRow


def findMirror(rowNumber, table):
    (foundSmudge, leftRow, rightRow), separation = checkForSmudge(False, table[rowNumber], table[rowNumber + 1]), 0
    while leftRow == rightRow:
        separation += 1
        if (rowNumber - separation) < 0 or (rowNumber + 1 + separation) >= len(table):
            return rowNumber + 1 if foundSmudge else 0
        foundSmudge, leftRow, rightRow = checkForSmudge(foundSmudge, table[rowNumber - separation],
                                                        table[rowNumber + 1 + separation])
    return 0


def getResForTable(table):
    for rowNumber in range(len(table) - 1):
        leftOfMirror = findMirror(rowNumber, table)
        if leftOfMirror:
            return leftOfMirror
    return 0


def getResForAxis(tables):
    return sum(map(getResForTable, tables))


def getResult():
    data = [table.split("\n") for table in open(os.path.join("input-data-2023", "23-13.txt")).read().split("\n\n")]
    transposedData = [[''.join(list(x)) for x in list(zip(*table))] for table in data]
    return 100*getResForAxis(data) + getResForAxis(transposedData)


print(getResult())
