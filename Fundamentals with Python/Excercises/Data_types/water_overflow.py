number_of_iterations = int(input())
capacity = 255
for iteration in range(number_of_iterations):
    liters_of_water = int(input())
    if capacity - liters_of_water < 0:
        print('Insufficient capacity!')
        continue
    capacity -= liters_of_water
print(255 - capacity)



