import os

day12 = [line.split() for line in open(os.path.join("input-data-2023", "23-12.txt")).read().strip().split("\n")]
day12 = [(sequence, combos.split(",")) for (sequence, combos) in day12]
res = 0
for sequence, combos in day12:
    sequenceLength, numOfCombos, stack, arrangements = len(sequence), len(combos), [], 0
    # stack schema: (seqSoFar, nextSeqCharIdx, nextComboIdx, comboJustCaught)
    stack.append(("", 0, 0, False))
    while stack:
        # pop stack to get next entry under consideration
        seqSoFar, nextSeqCharIdx, nextComboIdx, comboJustCaught = stack.pop()
        # if nextSeqCharIdx and nextComboIdx are both out of range, this is valid res so increment arrangements
        if nextSeqCharIdx >= sequenceLength and nextComboIdx >= numOfCombos:
            arrangements += 1
            print(seqSoFar)
        # if nextSeqCharIdx is out of range but nextComboIdx is not, this is an invalid res so continue
        elif nextSeqCharIdx >= sequenceLength and nextComboIdx < numOfCombos:
            continue
        # if nextSeqCharIdx is not out of range but nextComboIdx is:
        elif nextSeqCharIdx < sequenceLength and nextComboIdx >= numOfCombos:
            # if next char is "#", this is invalid res so continue.
            # otherwise add new stack entry with incremented nextSeqIdxChar & updated seqSoFar with "." and continue
            if sequence[nextSeqCharIdx] != "#":
                stack.append((seqSoFar + ".", nextSeqCharIdx + 1, nextComboIdx, False))
        # if neither are out of range:
        else:
            # if next char is not "?", check if it remains possible that seqSoFar can produce current combo next.
            if sequence[nextSeqCharIdx] != "?":
                newChar = sequence[nextSeqCharIdx]
                if newChar == ".":
                    if (not seqSoFar) or (not ((not comboJustCaught) and (seqSoFar[-1] == "#"))):
                        stack.append((seqSoFar + ".", nextSeqCharIdx + 1, nextComboIdx, False))
                else:
                    # check if new "#" interferes with previous combo - if so continue
                    if comboJustCaught:
                        continue
                    # check if new "#" has done the job
                    if len(seqSoFar + "#") >= int(combos[nextComboIdx]) and len(set((seqSoFar + "#")[-int(combos[nextComboIdx]):])) == 1:
                        stack.append((seqSoFar + "#", nextSeqCharIdx + 1, nextComboIdx + 1, True))
                    else:
                        stack.append((seqSoFar + "#", nextSeqCharIdx + 1, nextComboIdx, False))
            # otherwise add new entry for seqSoFar with ".", and check if # can still work and add this too if so.
            else:
                if (not seqSoFar) or (not ((not comboJustCaught) and (seqSoFar[-1] == "#"))):
                    stack.append((seqSoFar + ".", nextSeqCharIdx + 1, nextComboIdx, False))
                if comboJustCaught:
                    continue
                if len(seqSoFar + "#") >= int(combos[nextComboIdx]) and len(set((seqSoFar + "#")[-int(combos[nextComboIdx]):])) == 1:
                    stack.append((seqSoFar + "#", nextSeqCharIdx + 1, nextComboIdx + 1, True))
                else:
                    stack.append((seqSoFar + "#", nextSeqCharIdx + 1, nextComboIdx, False))
    res += arrangements

print(res)
