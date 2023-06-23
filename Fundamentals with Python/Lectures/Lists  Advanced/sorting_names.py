#--------------------CONDITION OF THE TASK------------------------------------------
#Write a program that reads a single string with names separated by comma and space ", ".
# Sort the names by their length in descending order.
# If 2 or more names have the same length,
# sort them in ascending order (alphabetically).
# Print the resulting list.


def sorting_names():
    names = input().split(', ')
    sorted_names = (sorted(names, key=lambda x: (-len(x), x)))
    return sorted_names

result = sorting_names()
print(result)


