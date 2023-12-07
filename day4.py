import os


def getCardValues(card):
    numbers = card.split(":")[1].strip().split("|")
    return set(map(int, numbers[0].split())), list(map(int, numbers[1].split()))


def updateCopiesForCard(cardNumber, cardValues, copies):
    (winningNumbers, givenNumbers), nextCard = cardValues, cardNumber + 1
    for number in givenNumbers:
        if number in winningNumbers:
            copies[nextCard] += copies[cardNumber]
            nextCard += 1
    return copies


def getResult():
    day4 = open(os.path.join("input-data-2023", "23-4.txt"))
    copies = {i: 1 for i in range(1, 224)}
    for i, card in enumerate(day4):
        copies = updateCopiesForCard(i+1, getCardValues(card), copies)
    return sum(copies.values())


print(getResult())
