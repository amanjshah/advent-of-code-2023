import os

day12 = [line.split() for line in open(os.path.join("input-data-2023", "23-12.txt")).read().strip().split("\n")]
res = 0
for sequence, combos in day12:
    sequenceLength, numOfCombos, sequenceIdx, combosIdx = len(sequence), len(combos), 0, 0
    stack, sequenceRes = [], 0
    # stack schema: (seqSoFar, nextSeqCharIdx, nextComboIdx, sequence, combos)
    # initialise stack here
    while stack:
        # pop stack to get next entry under consideration
        # if nextSeqCharIdx and nextComboIdx are both out of range, this is valid res so add 1 to sequenceRes
        # if nextSeqCharIdx is out of range but nextComboIdx is not, this is an invalid res so continue
        # if nextSeqCharIdx is not out of range but nextComboIdx is:
            # if next char is "#", this is invalid res so continue.
            # otherwise add new stack entry with incremented nextSeqIdxChar & updated seqSoFar with "." and continue
        # if neither are out of range:
            # if next char is not "?", check if it remains possible that seqSoFar can produce current combo next.
            # otherwise add new entry for seqSoFar with ".", and check if # can still work and add this too if so.
        pass
    res += sequenceRes