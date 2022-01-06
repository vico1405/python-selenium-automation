# When user enters a number, its factorial is displayed.

# Code here

import math

# 0(n)
number = int(input('Input your number: '))
# result = math.factorial(number)

result = 1
if number != 0:
    for i in range(1, number + 1):
        result = result * i  # result *= i

print(f'The factorial of {number} is {result}')
