import math
import os


def getData():
    workflowsBlock, ratingsBlock = [block.split("\n") for block in
                                    open(os.path.join("input-data-2023", "23-19.txt")).read().strip().split("\n\n")]
    workflows = {}
    for workflow in workflowsBlock:
        conditionsStart = workflow.find("{")
        key, conditions = workflow[:conditionsStart], workflow[conditionsStart + 1:-1].split(",")
        workflows[key] = []
        for condition in conditions[:-1]:
            targetStart = condition.find(":")
            category, comparison, value = condition[0], 0 if condition[1] == "<" else 1, int(condition[2:targetStart])
            workflows[key].append((category, comparison, value, condition[targetStart + 1:]))
        workflows[key].append(conditions[-1])
    return workflowsBlock, ratingsBlock, workflows


def getResult():
    (_, _, workflows), stack, res = getData(), [({key: (1, 4000) for key in "xmas"}, "in")], 0
    while stack:
        ranges, key = stack.pop()
        if key in "AR":
            res = addToTotal(key, ranges, res)
        else:
            addToStack(key, ranges, stack, workflows)
    return res


def addToStack(key, ranges, stack, workflows):
    rules = workflows[key]
    for category, greaterThan, newBoundary, nextKey in rules[:-1]:
        minValue, maxValue = ranges[category]
        lowerBound, upperBound, prevBoundary = ((newBoundary + 1, maxValue, minValue) if greaterThan
                                                else (minValue, newBoundary - 1, maxValue))
        if lowerBound <= upperBound:
            nextRanges = dict(ranges)
            nextRanges[category] = (lowerBound, upperBound)
            stack.append((nextRanges, nextKey))
        if (greaterThan and prevBoundary <= newBoundary) or (not greaterThan and newBoundary <= prevBoundary):
            ranges[category] = (prevBoundary, newBoundary) if greaterThan else (newBoundary, prevBoundary)
        else:
            break
    else:
        stack.append((ranges, rules[-1]))


def addToTotal(key, ranges, currentTotal):
    return currentTotal + (math.prod(map(lambda vals: vals[1] - vals[0] + 1, ranges.values())) if key == "A" else 0)


print(getResult())
