#Function exercise 7 Small

def only_odds(numList):
    odds = []
    for num in numList:
        if not(num % 2 == 0):
            odds.append(num)
    return odds
numList = [1, 3, 4, 6, 7, 10, 14]
print(only_odds(numList))