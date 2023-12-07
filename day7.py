import os
from enum import Enum
from heapq import heappush, heappop
from collections import Counter


class Node:
    order = {"A": 4, "K": 3, "Q": 2, "T": 1}

    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid

    def priority(self, selfChar, otherChar):
        if selfChar == "J" or (selfChar.isdigit() and not otherChar.isdigit() and otherChar != "J"):
            return True
        if otherChar == "J" or (otherChar.isdigit() and not selfChar.isdigit()):
            return False
        if selfChar.isdigit() and otherChar.isdigit():
            return selfChar < otherChar
        return self.order[selfChar] < self.order[otherChar]

    def __lt__(self, other):
        for i in range(5):
            selfChar, otherChar = self.hand[i], other.hand[i]
            if selfChar != otherChar:
                return self.priority(selfChar, otherChar)
        return True


class Type(Enum):
    HIGH = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FULL = 4
    FOUR = 5
    FIVE = 6


def getData():
    return [line.split() for line in open(os.path.join("input-data-2023", "23-7.txt")).read().strip().split("\n")]


def getTypeForHand(counts):
    mostCommonCards = [count for (card, count) in counts.most_common() if card != "J"]
    jokerCount = counts["J"]
    if not mostCommonCards or (mostCommonCards[0] + jokerCount >= 5):
        return Type.FIVE
    if mostCommonCards[0] + jokerCount >= 4:
        return Type.FOUR
    if mostCommonCards[0] + mostCommonCards[1] + jokerCount >= 5:
        return Type.FULL
    if mostCommonCards[0] + jokerCount >= 3:
        return Type.THREE
    if mostCommonCards[0] + mostCommonCards[1] + jokerCount >= 4:
        return Type.TWO
    if mostCommonCards[0] + jokerCount >= 2:
        return Type.ONE
    return Type.HIGH


def getPriorityQueues(hands):
    types = {handType: [] for handType in Type}
    for hand, bid in hands:
        heappush(types[getTypeForHand(Counter(hand))], Node(hand, bid))
    return types


def calculateWinnings(types):
    winnings, rank = 0, 1
    for handType in Type:
        nodes = types[handType]
        while nodes:
            winnings += int(heappop(nodes).bid) * rank
            rank += 1
    return winnings


def getResult():
    return calculateWinnings(getPriorityQueues(getData()))


print(getResult())
