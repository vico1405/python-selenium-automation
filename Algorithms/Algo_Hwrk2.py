# Given a string. Split it into two equal parts.
# Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’

'''# Original string
test_str = "bbbbbcaaaaa"

# printing original string
print("The original string is : " + test_str)

def split_in_equal(x):
    Total = len(x)
    A = Total // 2
    i = 0

    if Total % 2:
        i = 1
    res_first = x[:A + i]
    res_second = x[A + 1:]
    return res_second + res_first

test_str_odd = 'aaabccc'
test_str_even = 'aaabbb'
print(test_str_odd)
print(split_in_equal(test_str_odd))
print(test_str_even)
print(split_in_equal(test_str_even))'''

2
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

def unic_char(str):
    # if character has duplicate, return false

    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i] == str[j]):
                return False;

    # if no duplicate character return True
    return True;
# character strings
str = "WordforWords"

if(unic_char(str)):
    print("The String ", str, "has all unique characters")
else:
    print("The string ", str, "has duplicate characters")

