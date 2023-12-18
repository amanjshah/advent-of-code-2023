import os


def getCoordinates(data, incrementation):
    coordinates, boundaryPoints = [(0, 0)], 0
    for _, _, colour in data:
        steps = int(colour[:-1], 16)
        di, dj = (delta * steps for delta in incrementation[int(colour[-1])])
        boundaryPoints += steps
        i, j = coordinates[-1]
        coordinates.append((i + di, j + dj))
    return coordinates, boundaryPoints


def getResult():
    data = [(line[0], int(line[2:4]), line[line.find("#")+1:-1]) for line in
            open(os.path.join("input-data-2023", "23-18.txt")).read().strip().split("\n")]
    incrementation = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    coordinates, boundaryPoints = getCoordinates(data, incrementation)
    # Shoelace formula to calculate area
    area = abs(sum(
        coordinates[i][0] * (coordinates[i + 1][1] - coordinates[i - 1][1]) for i in range(len(coordinates) - 1))) / 2
    # Pick's theorem to get number of grid squares contained within boundary
    interiorPoints = area - (boundaryPoints / 2) + 1
    return boundaryPoints + interiorPoints


print(getResult())
