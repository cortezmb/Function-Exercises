#Function exercise 6 Small

def only_evens(numList):
    evens = []
    for num in numList:
        if num % 2 == 0:
            evens.append(num)
    return evens
numList = [1, 3, 4, 6, 7, 10, 14]
print(only_evens(numList))

