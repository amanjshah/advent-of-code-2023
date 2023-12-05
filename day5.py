import os

# Monstrous
day5 = open(os.path.join("input-data-2023", "23-5.txt"))


def getSeeds(data):
    nums = list(map(int, data[0].strip().split(": ")[1].split()))
    return [(nums[i], nums[i] + nums[i + 1]) for i in range(0, len(nums), 2)]


def getBlocks(data):
    block, blocks = [], []
    for line in data[3:]:
        if not line:
            blocks.append(block)
            block = []
        elif line[0].isdigit():
            dest, src, length = tuple(map(int, line.split()))
            block.append((src, src + length, dest - src))
    blocks.append(block)
    return blocks


def getLocations(ranges, blocks):
    for block in blocks:
        # store ranges introduced by mappings in this block separately to the ranges that were previously present
        # these must be mapped by ranges they overlap with in subsequent blocks, but not in this block
        newRanges = []
        updateRangesForBlock(block, ranges, newRanges)
        ranges = newRanges
    return ranges


def updateRangesForBlock(block, ranges, newRanges):
    while ranges:
        start, end = ranges.pop()
        for srcStart, srcEnd, mapping in block:
            if min(end, srcEnd) > max(start, srcStart):  # if there is overlap...
                # add a new range for overlapping values
                newRanges.append((max(start, srcStart) + mapping, min(end, srcEnd) + mapping))
                # add back non-overlapping values to current list of ranges
                # these still need to be accounted for if they overlap with other mappings in current block
                if srcStart > start:
                    ranges.append((start, srcStart))
                if end > srcEnd:
                    ranges.append((srcEnd, end))
                break
        else:
            newRanges.append((start, end))


def getResult(dayFiveData):
    data = [line.strip() for line in dayFiveData]
    blocks = getBlocks(data)
    seeds = getSeeds(data)
    return min(getLocations(seeds, blocks))[0]


print(getResult(day5))
