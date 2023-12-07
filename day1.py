import os


def categoriseByWordLength():
    wordDigits = {}
    for digit in ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine"):
        charCount = len(digit)
        if charCount in wordDigits:
            wordDigits[charCount].add(digit)
        else:
            wordDigits[charCount] = {digit}
    return wordDigits


DIGITS_OF_SIZE = categoriseByWordLength()
WORD_TO_DIGIT = {"one": "1", "two": "2", "three": "3",
                 "four": "4", "five": "5", "six": "6",
                 "seven": "7", "eight": "8", "nine": "9"}


def getDigit(line, i):
    if line[i].isdigit():
        return line[i]
    for wordSize in (3, 4, 5):
        if i <= len(line) - wordSize and line[i:i + wordSize] in DIGITS_OF_SIZE[wordSize]:
            return WORD_TO_DIGIT[line[i:i + wordSize]]


def getCalibrationValue(line):
    firstDigit, firstDigitIdx = getToDigit(line, 0, len(line), 1)
    secondDigit, _ = getToDigit(line, len(line) - 1, firstDigitIdx - 1, -1)
    return int(firstDigit + secondDigit)


def getToDigit(line, start, stop, increment):
    for i in range(start, stop, increment):
        digit = getDigit(line, i)
        if digit:
            return digit, i


def getResult():
    return sum(getCalibrationValue(line) for line in open(os.path.join("input-data-2023", "23-1.txt")))


print(getResult())
