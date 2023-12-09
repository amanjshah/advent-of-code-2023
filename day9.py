import os


def getSequences():
    return [list(map(int, line.split())) for line in
            open(os.path.join("input-data-2023", "23-9.txt")).read().strip().split("\n")]


def extrapolateSequence(sequence):
    res, sequences = getBaseDifference(sequence)
    return res + sum(differences[-1] for differences in sequences[::-1])


def getBaseDifference(sequence):
    sequences, differences = [], sequence[::-1]
    while len(set(differences)) != 1:
        sequences.append(differences)
        differences = [differences[i+1] - differences[i] for i in range(len(differences) - 1)]
    return differences[0], sequences


def getResult():
    return sum(map(extrapolateSequence, getSequences()))


print(getResult())
