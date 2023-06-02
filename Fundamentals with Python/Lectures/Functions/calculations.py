# --------------------------CONDITION OF THE TASK--------------------------------
# Create a function that receives three parameters, calculates a result depending on the given operator,
# and returns it. Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers.
# The operator can be one of the following: "multiply", "divide", "add", "subtract".



def calculations():
    operator = input()
    num_1 = int(input())
    num_2 = int(input())
    result = 0
    if operator == 'multiply':
        result = num_1 * num_2
        return result
    elif operator == 'divide':
        if num_2 != 0:
            result = num_1 / num_2
            return f'{result:.0f}'
    elif operator == 'add':
        result = num_1 + num_2
        return result
    elif operator == 'subtract':
        result = num_1 - num_2
        return result


print(calculations())