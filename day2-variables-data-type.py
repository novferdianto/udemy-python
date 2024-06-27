two_digit_number = input("Type a two digit number: ")
# check data-type for this input
print(type(two_digit_number))

# convert input from string to integer, and put string position 0 into variable first_digit and string position 1 into variable second_digit
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# add the two variables and print the result
result = first_digit + second_digit
print(result)


# Mathematical Operations in Python
# PEMDAS
# Parenthesis ()
print((3+3)*2)
# Exponents **
print(3**4)
# Multiplication *
print(3*4)
# Division /
print(3/4)
# Addition +
print(3+4)
# Substraction -
print(3-4)
# This is how using mathematical operation in python
