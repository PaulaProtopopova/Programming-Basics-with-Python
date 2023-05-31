list = input().split()
opposite_list = []
for index in range(len(list)):
    element = list[index]
    opposite_list.append(-int(element))
print(opposite_list)
