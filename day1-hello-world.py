#This is how using print() function in python
#Always rename to main.py for replit to run
print("Hello World")

#This is how using print() function and concatenating strings in python
print("Hello " + "World")

#This is how using print() function, concating strings and adding double quotes in python
print("Hello " + "World ." + "this is using \"double quotes\"")

#This is how using print() function and taking input from user in python
print("Hello " + input("What is your name ? "))

#This is how using print() function and taking input from user and calculating the length of the input in python
print("Hello " +  " your name has " + str(len(input("What is your name ? "))) + " characters") 

#This is how using print() function and taking input from user and store into variable in python
name = input("What is your name ? ")
print("Hello " + name)

#This is how using print() function and taking input from user, store into variable and calculating the length of the input from the variable in python
nama = input("What is your name ? ")
length = len(nama)
print(length)

#This is how using temporary variable in python
var_a = input("variable a: ")
var_b = input("variable b: ")
temp = var_a
var_a = var_b
var_b = temp
print("variable a : " + var_a)
print("variable b : " + var_b)