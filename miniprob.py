# #1 Swapping values with out temp variables
# a = 50
# b = 70

# a = a+b #120
# b = a-b #50
# a = a-b #70

# print("After swapping: a = ",a ,"b = ",b)





# Key Points:
# Floating-Point Representation:

# Numbers like 0.1, 0.2, and 0.3 cannot be represented exactly in binary. Instead, they are stored as approximations, which leads to rounding errors.
# These errors occur because some decimal fractions cannot be represented as finite binary fractions (similar to how 1/3 in decimal is a repeating fraction: 0.333...).
# Languages with Similar Behavior: The issue of 0.1 + 0.2 != 0.3 happens in most programming languages, including but not limited to:

# C
# C++
# Java
# JavaScript
# C#
# Ruby
# Go
# PHP
# Swift





if(0.1+0.2 == 0.3):
    print('True')
else:
    print('False')


if(0.1+0.1 == 0.2):
    print('True')
else:
    print('False')

if(0.1+0.3 == 0.4):
    print('True')
else:
    print('False')



