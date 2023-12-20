import os
from collections import deque


def getData():
    data = [line.split(" -> ") for line in
            open(os.path.join("input-data-2023", "23-20.txt")).read().strip().split("\n")]
    modulesMap = dict((mapping[0][1:], mapping[1].split(", ")) if mapping[0][0] in "%&"
                      else (mapping[0], mapping[1].split(", ")) for mapping in data)
    flipflops = dict((module, False) for module in set(map(lambda module: module[0][0] == "%" and module[0][1:], data)))
    conjunctions = dict((module, []) for module in set(map(lambda module: module[0][0] == "&" and module[0][1:], data)))
    flipflops.pop(False, None)
    conjunctions.pop(False, None)
    for module in modulesMap:
        for nextModule in modulesMap[module]:
            if nextModule in conjunctions:
                conjunctions[nextModule].append([module, False])
    return modulesMap, flipflops, conjunctions

modulesMap, flipflops, conjunctions = getData()
flipflopsList, conjunctionsList = list(dict(flipflops).keys()), list(dict(conjunctions).keys())
buttonPushes, lowSignals, highSignals, machineOn, cache = 0, 0, 0, False, {}
def hash(flipflops, conjunctions):
    hashableFlipflops = ''.join(["1" if flipflops[key] else "0" for key in flipflopsList])
    hashableConjunctions = tuple(''.join(["1" if lastReceived else "0" for (_, lastReceived)
                                          in conjunctions[node]]) for node in conjunctionsList)
    return hashableFlipflops, hashableConjunctions

hashableFlipflops, hashableConjunctions = hash(flipflops, conjunctions)
while not machineOn:
    newFlipflopsHash, newConjunctionsHash = hash(flipflops, conjunctions)
    if (hashableFlipflops == newFlipflopsHash or hashableConjunctions == newConjunctionsHash) and buttonPushes > 0:
        break
    buttonPushes += 1
    lowSignals += 1
    queue = deque([(node, False, "broadcaster") for node in modulesMap["broadcaster"]])
    while queue:
        module, signalInput, previous = queue.popleft()
        machineOn = machineOn or (module == "rx" and not signalInput)
        if signalInput:
            highSignals += 1
        else:
            lowSignals += 1
        if module in flipflops and not signalInput:
            flipflops[module] = not flipflops[module]
            for nextModule in modulesMap[module]:
                queue.append((nextModule, flipflops[module], module))
        elif module in conjunctions:
            for i in range(len(conjunctions[module])):
                if conjunctions[module][i][0] == previous:
                    conjunctions[module][i][1] = signalInput
            for inputModule, lastReceived in conjunctions[module]:
                if not lastReceived:
                    for nextModule in modulesMap[module]:
                        queue.append((nextModule, True, module))
                    break
            else:
                for nextModule in modulesMap[module]:
                    queue.append((nextModule, False, module))
print(buttonPushes, lowSignals, highSignals)