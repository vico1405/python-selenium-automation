# our code generates a random three-digit number and has to sum all its digits.
# For example, if a number is 349, the code has to print the number 16, because 3 + 4 + 9 = 16

from random import randint

random_number = randint(100, 999)
print(f'Our random number is {random_number}')

# solution 1
# result = 0
# for digit in str(random_number):
#    result = result + int(digit) # result += int(digit)

# Solution 2
# random number = 12
result = 0
while random_number != 0:
    result = result + (random_number % 10) # 2
    random_number = random_number // 10  # 2

print(f'Result of a sum: {result}')