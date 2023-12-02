import os

day1 = open(os.path.join("input-data-2023", "23-1.txt"))
        
def generateWordDigits():
    wordDigits = {}
    for digit in ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine"):
        charCount = len(digit)
        if charCount in wordDigits: wordDigits[charCount].add(digit)
        else: wordDigits[charCount] = {digit}
    return wordDigits

wordDigits = generateWordDigits()
digits = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def getDigit(line, i,):
    if line[i].isdigit(): return line[i]
    for wordSize in (3,4,5):
        if i <= len(line)-wordSize and line[i:i+wordSize] in wordDigits[wordSize]: return digits[line[i:i+wordSize]]
    return None
       
def getCalibrationValue(line):
    firstDigitIdx = 0
    
    firstDigit = None
    for i in range(len(line)):
        firstDigit = getDigit(line, i)
        if not firstDigit: continue
        firstDigitIdx = i
        break

    secondDigit = firstDigit
    for i in range(firstDigitIdx+1, len(line)):
        previousSecondDigit = secondDigit
        nextDigit = getDigit(line, i)
        secondDigit = nextDigit if nextDigit else secondDigit 
        if secondDigit == previousSecondDigit: continue

    return int(firstDigit + secondDigit)

def getResult(dayOneFile):
    res = 0
    for line in dayOneFile:
        res += getCalibrationValue(line)      
    return res


print(getResult(day1))