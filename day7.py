import os
import heapq
from collections import Counter


class Node:
    order = {"A": 4, "K": 3, "Q": 2, "T": 1}

    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid

    def __lt__(self, other):
        for i in range(5):
            if self.hand[i] == other.hand[i]:
                continue
            if self.hand[i] == "J":
                return True
            if other.hand[i] == "J":
                return False
            if self.hand[i].isdigit() and other.hand[i].isdigit():
                return self.hand[i] < other.hand[i]
            if self.hand[i].isdigit() and not other.hand[i].isdigit():
                return True
            if other.hand[i].isdigit() and not self.hand[i].isdigit():
                return False
            return self.order[self.hand[i]] < self.order[other.hand[i]]
        return True


def getData():
    return [line.split() for line in open(os.path.join("input-data-2023", "23-7.txt")).read().strip().split("\n")]


def getNodeData(hand, bid):
    counts = Counter(hand)
    return counts, Node(hand, bid), len(counts)


def pushNodeToHeap(counts, node, numOfUniqueCards, types):
    if numOfUniqueCards == 5:
        heapq.heappush(types["one"], node) if "J" in counts else heapq.heappush(types["high"], node)
    elif numOfUniqueCards == 4:
        heapq.heappush(types["three"], node) if "J" in counts else heapq.heappush(types["one"], node)
    elif numOfUniqueCards == 3:
        if 3 in counts.values():
            heapq.heappush(types["four"], node) if "J" in counts else heapq.heappush(types["three"], node)
        else:
            if counts["J"] == 2:
                heapq.heappush(types["four"], node)
            elif counts["J"] == 1:
                heapq.heappush(types["full"], node)
            else:
                heapq.heappush(types["two"], node)
    elif numOfUniqueCards == 2:
        if "J" in counts:
            heapq.heappush(types["five"], node)
        else:
            heapq.heappush(types["four"], node) if 4 in counts.values() else heapq.heappush(types["full"], node)
    else:
        heapq.heappush(types["five"], node)
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
            node = heapq.heappop(nodes)
            winnings += int(node.bid) * rank
            rank += 1
    return winnings


def getResult():
    hands = getData()
    types = getPriorityQueues(hands)
    return calculateWinnings(types)


print(getResult())
