# --------------------------------CONDITION OF THE TASK ----------------------------------------------
# Write a function that receives three integer numbers and returns the smallest. Print the result on the console.
# Use an appropriate name for the function.

def smallest_of_numbers(a, b, c):
    return min(a, b, c)


a = int(input())
b = int(input())
c = int(input())
print(smallest_of_numbers(a, b, c))

