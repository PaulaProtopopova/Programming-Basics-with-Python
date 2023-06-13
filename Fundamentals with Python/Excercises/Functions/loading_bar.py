# -----------------------CONDITION OF THE TASK----------------------
# You will receive a single integer number between 0 and 100 (inclusive)
# divisible by 10 without remainder (0, 10, 20, 30...).
# Your task is to create a function that returns a loading bar depending on
# the number you have received in the input.
# Print the result on the console.




def loading_bar(some_number):
    loading_bar = ['.''.''.''.''.''.''.''.''.''.']
    percents_count = some_number // 10
    if percents_count == 10:
        return f'{some_number}% Complete!\n[%%%%%%%%%%]'
    return f"{some_number}% [{'%' * percents_count}{'.' * (10 - percents_count)}]\nStill loading..."



number = int(input())
print(loading_bar(number))