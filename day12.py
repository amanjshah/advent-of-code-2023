import os

cache = {}


def getNumberOfArrangements(remainingSequence, nums):
    if (remainingSequence, nums) in cache:
        return cache[(remainingSequence, nums)]
    if not remainingSequence:
        return 0 if nums else 1
    if not nums:
        return 0 if "#" in remainingSequence else 1
    res, nextSymbol, nextNumber = 0, remainingSequence[0], nums[0]
    if nextSymbol in "?.":
        res += getNumberOfArrangements(remainingSequence[1:], nums)
    if nextSymbol in "?#":
        if (nextNumber <= len(remainingSequence) and "." not in remainingSequence[:nextNumber]
                and (nextNumber == len(remainingSequence) or remainingSequence[nextNumber] != "#")):
            res += getNumberOfArrangements(remainingSequence[nextNumber + 1:], nums[1:])
    cache[(remainingSequence, nums)] = res
    return res


def getResult():
    day12 = [line.split() for line in open(os.path.join("input-data-2023", "23-12.txt")).read().strip().split("\n")]
    data = [("?".join([sequence] * 5), tuple(map(int, nums.split(",") * 5))) for (sequence, nums) in day12]
    res = sum(map(lambda row: getNumberOfArrangements(row[0], row[1]), data))
    return res


print(getResult())
