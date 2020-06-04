#Functions exercise 2 Small
# Define my function and argument
def c2f(tempC):
    # Create a varable using argument variable
    tempF = (tempC * 9/5) + 32
    # Return the created variable
    return tempF
# Create a global memory variable that equals the function with an assigned value for argument
result = c2f(100)
# Print global memory variable. 
print(result)
