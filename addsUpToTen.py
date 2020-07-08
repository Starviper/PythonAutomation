import pyinputplus as pyip

def addsUpToTen(numbers):
    numberslist = list(numbers)
    for i, digit in enumerate(numberslist):
        numberslist[i] = int(digit)
    if sum(numberslist) != 10:
        raise Exception('The digits must add up to 10, not %s.' %(sum(numberslist)))
    return int(numbers) # Return an int form of numbers.