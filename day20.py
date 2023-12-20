from math import lcm
import os
from collections import deque


def getData():
    data = [line.split(" -> ") for line in
            open(os.path.join("input-data-2023", "23-20.txt")).read().strip().split("\n")]
    modulesMap = dict((mapping[0][1:], mapping[1].split(", ")) if mapping[0][0] in "%&"
                      else (mapping[0], mapping[1].split(", ")) for mapping in data)
    allFlipflops = {module: False for module in set(map(lambda module: module[0][0] == "%" and module[0][1:], data))}
    allConjunctions = {module: [] for module in set(map(lambda module: module[0][0] == "&" and module[0][1:], data))}
    allFlipflops.pop(False, None)
    allConjunctions.pop(False, None)
    for module in modulesMap:
        for nextModule in modulesMap[module]:
            if nextModule in allConjunctions:
                allConjunctions[nextModule].append([module, False])
    return modulesMap, allFlipflops, allConjunctions


MODULES_MAP, flipflops, conjunctions = getData()
CONJUNCTIONS_TO_SYNC = set(module for module in MODULES_MAP if "kz" in MODULES_MAP[module])


def addToQueue(queue, module, outputSignal, cycleLengths, buttonPushes):
    for nextModule in MODULES_MAP[module]:
        if nextModule == "kz" and outputSignal and module not in cycleLengths:
            # kz outputs to rx & is a conjunction, i.e. outputs low if it last received high from all inputs
            # assume cyclical patterns for incoming signals to kz from each of its inputs:
            cycleLengths[module] = buttonPushes
        queue.append((nextModule, outputSignal, module))


def updateConjunctions(inputSignal, module, previous):
    for i in range(len(conjunctions[module])):
        if conjunctions[module][i][0] == previous:
            conjunctions[module][i][1] = inputSignal


def addConjunctionToQueue(buttonPushes, cycleLengths, module, queue):
    for inputModule, lastReceived in conjunctions[module]:
        if not lastReceived:
            addToQueue(queue, module, True, cycleLengths, buttonPushes)
            break
    else:
        addToQueue(queue, module, False, cycleLengths, buttonPushes)


def pushButton(buttonPushes, cycleLengths):
    queue = deque([(node, False, "broadcaster") for node in MODULES_MAP["broadcaster"]])
    while queue:
        module, inputSignal, previous = queue.popleft()
        if module in flipflops and not inputSignal:
            flipflops[module] = not flipflops[module]
            addToQueue(queue, module, flipflops[module], cycleLengths, buttonPushes)
        elif module in conjunctions:
            updateConjunctions(inputSignal, module, previous)
            addConjunctionToQueue(buttonPushes, cycleLengths, module, queue)


def getResult():
    cycleLengths, buttonPushes = {}, 0
    while len(CONJUNCTIONS_TO_SYNC) > len(cycleLengths):
        buttonPushes += 1
        pushButton(buttonPushes, cycleLengths)
    return lcm(*cycleLengths.values())


print(getResult())
