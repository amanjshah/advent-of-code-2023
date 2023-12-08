from math import lcm
import os


def getData():
    day8 = open(os.path.join("input-data-2023", "23-8.txt")).read().split("\n")
    mappings = dict((node, tuple(nextNodes[1:-1].split(", "))) for (node, nextNodes)
                    in [mapping.split(" = ") for mapping in day8[2:-1]])
    return day8[0], mappings, (node for node in mappings if node[-1] == "A")


def getSteps(node, sequence, mappings):
    steps = 0
    while node[-1] != "Z":
        for direction in sequence:
            node = mappings[node][0 if direction == "L" else 1]
            steps += 1
    return steps


def getResult():
    sequence, mappings, startingPoints = getData()
    # Each starting point only hits one of the {X}{X}Z endpoints
    # Next nodes for each endpoint are the next nodes for the corresponding starting point
    # Therefore single cycle per starting point input, so use lcm
    return lcm(*map(lambda startingPoint: getSteps(startingPoint, sequence, mappings), startingPoints))


print(getResult())
