n = int(input())
special_word = input()
lst = list()
filtered_lst = list()

for _ in range(n):
    string = input()
    lst.append(string)
    if special_word in string:
        filtered_lst.append(string)
print(lst)
print(filtered_lst)