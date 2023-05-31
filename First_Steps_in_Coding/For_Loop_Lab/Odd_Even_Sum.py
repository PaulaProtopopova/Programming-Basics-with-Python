n = int(input())
even_sum = 0
odd_sum = 0

for num in range(n):
    current_num = int(input())
    if num % 2 == 0:
        even_sum += current_num
    else:
        odd_sum += current_num
diff = abs(odd_sum-even_sum)
if even_sum == odd_sum:
    print(f"Yes")
    print(f"Sum = {even_sum}")
else:
    print(f"No")
    print(f"Diff = {diff}")