#Functions exercise 1 Medium
def smallest(numList):
    numList = []
    smallNum = numList[0]
    for num in numList:
        if num < smallNum:
            smallNum = num
            return smallNum
            numlist.append(smallNum)
        
numList = [1, 8, 4, 20, 14, 7]
print(smallest(numList))

