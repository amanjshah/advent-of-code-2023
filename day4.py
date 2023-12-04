import os

day4 = open(os.path.join("input-data-2023", "23-4.txt"))
copies = {i: 1 for i in range(1, 224)}


def getCardValues(card):
    numbers = card.split(":")[1].strip().split("|")
    return set(map(int, numbers[0].split())), list(map(int, numbers[1].split()))


def updateCopiesForCard(cardNumber, winningNumbers, givenNumbers):
    nextCard = cardNumber + 1
    for number in givenNumbers:
        if number in winningNumbers:
            copies[nextCard] += copies[cardNumber]
            nextCard += 1


def getResult(dayFourFile):
    cardNumber = 0
    for card in dayFourFile:
        cardNumber += 1
        winningNumbers, givenNumbers = getCardValues(card)
        updateCopiesForCard(cardNumber, winningNumbers, givenNumbers)
    return sum(copies.values())


print(getResult(day4))
