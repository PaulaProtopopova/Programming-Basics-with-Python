length = int(input())
width = int(input())
height = int(input())
percent_accessories = float(input())

volume_of_the_tank = length * width * height
litres_of_the_tank = volume_of_the_tank / 1000

filled_space = (percent_accessories / 100) * litres_of_the_tank
litres_water = litres_of_the_tank - filled_space

print(litres_water)
