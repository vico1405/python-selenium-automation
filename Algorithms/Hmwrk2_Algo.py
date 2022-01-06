# Python program to find the largest
# number among the three numbers

def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest


# Driven code
a = 15
b = 17
c = 20
print(maximum(a, b, c))
