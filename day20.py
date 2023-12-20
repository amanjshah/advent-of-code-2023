from math import lcm
import os
from collections import deque


def getData():
    data = [line.split(" -> ") for line in
            open(os.path.join("input-data-2023", "23-20.txt")).read().strip().split("\n")]
    modulesMap = dict((mapping[0][1:], mapping[1].split(", ")) if mapping[0][0] in "%&"
                      else (mapping[0], mapping[1].split(", ")) for mapping in data)
    flipflops = {module: False for module in set(map(lambda module: module[0][0] == "%" and module[0][1:], data))}
    conjunctions = {module: [] for module in set(map(lambda module: module[0][0] == "&" and module[0][1:], data))}
    flipflops.pop(False, None)
    conjunctions.pop(False, None)
    for module in modulesMap:
        for nextModule in modulesMap[module]:
            if nextModule in conjunctions:
                conjunctions[nextModule].append([module, False])
    return modulesMap, flipflops, conjunctions


MODULES_MAP, FLIPFLOPS, CONJUNCTIONS = getData()
CONJUNCTIONS_TO_SYNC = set(module for module in MODULES_MAP if "kz" in MODULES_MAP[module])


def addToQueue(queue, module, outputSignal, cycleLengths, buttonPushes):
    for nextModule in MODULES_MAP[module]:
        if nextModule == "kz" and outputSignal and module not in cycleLengths:
            # kz outputs to rx & is a conjunction, i.e. outputs low if it last received high from all inputs
            # assume cyclical patterns for incoming signals to kz from each of its inputs:
            cycleLengths[module] = buttonPushes
        queue.append((nextModule, outputSignal, module))


def addConjunctionToQueue(queue, module, previousModule, inputSignal, cycleLengths, buttonPushes):
    for i in range(len(CONJUNCTIONS[module])):
        if CONJUNCTIONS[module][i][0] == previousModule:
            CONJUNCTIONS[module][i][1] = inputSignal
    for inputModule, lastReceived in CONJUNCTIONS[module]:
        if not lastReceived:
            addToQueue(queue, module, True, cycleLengths, buttonPushes)
            break
    else:
        addToQueue(queue, module, False, cycleLengths, buttonPushes)


def addFlipflopToQueue(queue, module, cycleLengths, buttonPushes):
    FLIPFLOPS[module] = not FLIPFLOPS[module]
    addToQueue(queue, module, FLIPFLOPS[module], cycleLengths, buttonPushes)


def getResult():
    cycleLengths, buttonPushes = {}, 0
    while len(CONJUNCTIONS_TO_SYNC) > len(cycleLengths):
        buttonPushes += 1
        queue = deque([(node, False, "broadcaster") for node in MODULES_MAP["broadcaster"]])
        while queue:
            module, inputSignal, previous = queue.popleft()
            if module in FLIPFLOPS and not inputSignal:
                addFlipflopToQueue(queue, module, cycleLengths, buttonPushes)
            elif module in CONJUNCTIONS:
                addConjunctionToQueue(queue, module, previous, inputSignal, cycleLengths, buttonPushes)
    return lcm(*cycleLengths.values())


print(getResult())
