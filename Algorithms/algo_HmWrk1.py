# Compute the sum of digits in all numbers from 1 to n.
# When a user enters a number n, find the sum of digits in all numbers from 1 to n.

# Returns sum of all digits in numbers
# from 1 to n

# 0(n)
'''def sumOfDigitsFrom1ToN(n) :
    result = 0  # initialize result

    # One by one compute sum of digits
    # in every number from 1 to n
    for x in range(1, n + 1):
        result = result + x

    return result

number = int(input('input a number: '))
print(sumOfDigitsFrom1ToN(number))'''

# 0(1)
'''def sum(n):
    final_result = (n * (n + 1)) / 2
    return final_result


number = int(input('input a number: '))
print(sum(number))'''


# Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124.

'''def find_max(n1, n2, n3):
    return max(n1, n2, n3)


n1 = int(input('Input value1: '))
n2 = int(input('Input value2: '))
n3 = int(input('Input value3: '))

print(find_max(n1, n2, n3))'''

# 0(1)
'''def find_max(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    if n2 > n1 and n2 > n3:
        return  n2
    return n3


n1 = int(input('Input value1: '))
n2 = int(input('Input value2: '))
n3 = int(input('Input value3: '))

print(find_max(n1, n2, n3))'''


# 0(n)
# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5)

'''def count_even_odd(n):
    even = 0
    odd = 0

    while n != 0:
        current_digit = n % 10
        if current_digit % 2:
            odd += 1
        else:
            even += 1

        n = n // 10

    return ["Evens: " + str(even),  "Odds: " + str(odd)]

numbers = int(input('Input a number: '))
print(count_even_odd(numbers))'''


