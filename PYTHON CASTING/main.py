"""# There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

# Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
Example
Integers:
"""

a = int(10)   # x will be 10
b = int(3.8) # y will be 3
c = int("3") # z will be 3

print(a)
print(b)
print(c)


#  you can do the same for float numbers

a = float(1)# will result to 1.0
b = float(7.9) # will result to 7.9
c = float('4') # will result to 4.0


# we can aslo do the same for strings

a = str(4) # this result to "4"
b = str(5.6) # will result to "5.6
c = str("my name is joseph") # will result to "my name is joseph"