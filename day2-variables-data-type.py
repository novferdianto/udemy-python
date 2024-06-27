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
# PEMDASLR  -> priority math calculation Left To Rigth and see the highest priority from Parenthesis to Substraction
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
# PEMDASLR example
# it will print 7
print(3 * 3 + 3 / 3 - 3)

# auto convert from float to int if we use // 
print(8 // 3)

#inserting different data types and print it without converting to similar data types, using f-string on print() function
score = 0
height = 1.70
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")