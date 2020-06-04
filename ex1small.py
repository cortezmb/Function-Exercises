#Function exercise 1 Small
def madlib(fName, subject):
    if fName <= " " or subject <= " ":
        print("You must love all subjects.")
    else:
        return f"{fName} loves learning {subject}."
    
result = madlib("Michael", "Python3")
print(result)
