#Function exercise 5 Small
def is_odd(someNum):
    if not(someNum % 2 == 0):
        return "Odd" 
    else:
        return "Even"
result = is_odd(10002926587)
print(result)
