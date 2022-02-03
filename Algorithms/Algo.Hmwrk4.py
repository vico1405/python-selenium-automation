# Your input is an array of integers, and you have to reorder its entries so that the even
# entries appear first. You are required to solve it without
# allocating additional storage (operate with the input array).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def input_integer(arr):
    Even = 0
    Odd = len(arr) - 1

    while Even < Odd:
        if arr[Even] % 2 == 0:
            Even += 1
        else:
            arr[Even], arr[Odd] = arr[Odd], arr[Even]
            Odd -= 1
    return arr
I = [7, 3, 5, 6, 4, 10, 3, 2]
I.sort(key=lambda n: n % 2 != 0)
print(I)   # Return [6, 4, 10, 2, 7, 3, 5, 3]


# A program that takes as input an array of digits
# encoding a nonnegative decimal integer D and
# updates the array to represent the integer D + 1.
#  For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

def AddOne(digits):

    # initialize index (digit of unit)
    index = len(digits) - 1
    while (index >= 0 and digits[index] == 9):
        digits[index] = 0
        index -= 1
    # if index < 0 (if all digits were 9)
    if (index < 0):

        digits.insert(0, 1)

    else:
        digits[index]+=1

    digits = [1, 2, 9]

    AddOne(digits)

    for digit in digits:
        print(digit, end='')

