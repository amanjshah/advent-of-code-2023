import os
from heapq import heappush, heappop
from collections import Counter


class Node:
    order = {"A": 4, "K": 3, "Q": 2, "T": 1}

    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid

    def __lt__(self, other):
        for i in range(5):
            selfChar, otherChar = self.hand[i], other.hand[i]
            if selfChar != otherChar:
                if selfChar == "J" or (selfChar.isdigit() and not otherChar.isdigit() and otherChar != "J"):
                    return True
                if otherChar == "J" or (otherChar.isdigit() and not selfChar.isdigit()):
                    return False
                if selfChar.isdigit() and otherChar.isdigit():
                    return self.hand[i] < other.hand[i]
                return self.order[selfChar] < self.order[otherChar]
        return True


def getData():
    return [line.split() for line in open(os.path.join("input-data-2023", "23-7.txt")).read().strip().split("\n")]


def getNodeData(hand, bid):
    counts = Counter(hand)
    return counts, Node(hand, bid), len(counts)


def pushNodeToHeap(counts, node, numOfUniqueCards, types):
    if numOfUniqueCards == 5:
        heappush(types["one"], node) if "J" in counts else heappush(types["high"], node)
    elif numOfUniqueCards == 4:
        heappush(types["three"], node) if "J" in counts else heappush(types["one"], node)
    elif numOfUniqueCards == 3:
        if 3 in counts.values():
            heappush(types["four"], node) if "J" in counts else heappush(types["three"], node)
        else:
            if counts["J"] == 2:
                heappush(types["four"], node)
            elif counts["J"] == 1:
                heappush(types["full"], node)
            else:
                heappush(types["two"], node)
    elif numOfUniqueCards == 2:
        if "J" in counts:
            heappush(types["five"], node)
        else:
            heappush(types["four"], node) if 4 in counts.values() else heappush(types["full"], node)
    else:
        heappush(types["five"], node)
    return types


def getPriorityQueues(hands):
    types = {handType: [] for handType in ("high", "one", "two", "three", "full", "four", "five")}
    for hand, bid in hands:
        counts, node, numOfUniqueCards = getNodeData(hand, bid)
        types = pushNodeToHeap(counts, node, numOfUniqueCards, types)
    return types


def calculateWinnings(types):
    winnings, rank = 0, 1
    for handType in ("high", "one", "two", "three", "full", "four", "five"):
        nodes = types[handType]
        while nodes:
            node = heappop(nodes)
            winnings += int(node.bid) * rank
            rank += 1
    return winnings


def getResult():
    hands = getData()
    types = getPriorityQueues(hands)
    return calculateWinnings(types)


print(getResult())
