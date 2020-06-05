#Functions exercise 3 small
# Define my function and argument
def f2c(tempF):
    # Create a varable using argument variable
    tempC = (tempF - 32) * 32
    # Return the created variable
    return tempC
# Create a global memory variable that equals the function with an assigned value for argument
result = f2c(32)
# Print global memory variable. 
print(result)