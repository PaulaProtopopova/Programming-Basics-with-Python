# ------------------------------------CONDITION OF THE TASK-------------------------------------
# You will receive two lines of input:
# •	a list of employees' happiness as a string of numbers separated by a single space
# •	a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# •	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"



happiness_points = list(map(int, input().split()))
factor = int(input())

def general_happiness_check():
    multiplied = [x * factor for x in happiness_points]
    average_happiness = sum(multiplied) / len(multiplied)
    the_happiest = [x for x in multiplied if x >= average_happiness]
    if len(the_happiest) >= len(multiplied) / 2:
        return f'Score: {len(the_happiest)}/{len(multiplied)}. Employees are happy!'
    else:
        return f'Score: {len(the_happiest)}/{len(multiplied)}. Employees are not happy!'

print(general_happiness_check())
