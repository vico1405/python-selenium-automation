# Compute the sum of digits in all numbers from 1 to n.
# When a user enters a number n, find the sum of digits in all numbers from 1 to n.

# Returns sum of all digits in numbers
# from 1 to n
def sumOfDigitsFrom1ToN(n) :
    result = 0  # initialize result

    # One by one compute sum of digits
    # in every number from 1 to n
    for x in range(1, n + 1):
        result = result + sumOfDigits(x)

    return result



