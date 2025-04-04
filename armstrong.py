# Program to find if a number is an Armstrong number or not and it is O(n) time compexity

num = int(input("Enetr Your Number:"))

digit_length = len(str(num))

result_number = 0

temp = num

while temp > 0:
    digit = temp % 10
    result_number += digit**digit_length
    temp //= 10

if (num == result_number):
    print(f"{num} is a armstrong number!")

else:
    print(f"{num} is not a armstrong number!")