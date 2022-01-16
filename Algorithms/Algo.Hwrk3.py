# (1)
# When given a list, the program should return a list of all the elements below the original
# list’s arithmetical mean. The arithmetical mean is
# the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

# importing mean()
from  statistics import  mean

def arithemetic_mean(lst):
    return mean(lst)

# Code
lst = [1, 3, 5, 6, 4, 10, 2, 3]
average =arithemetic_mean(lst)

# print the average list
print("arithemetic_mean =", round(average, 2))

# (2)

# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
import lib2to3.pgen2.token

lists = [198, 3, 4, 9, 10, 9, 2]

ln = float('inf')  # lowest number
sln = float('inf')  # second lowest number

for list in lists:
    if list <= ln:
        ln, sln = list, ln
    elif list < sln:
        sln = list
print(ln)
print(sln)










9
