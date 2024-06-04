# # python formating is done to allow compactibility with other data types
# we can combine strings and numbers by using the format() method!

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

#example
age = 36
name = "My name is John, and I am {} years old"
print(name.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

# Example
number = 3
itemnum = 567
price = 49.95
myorder = "I want {} pieces of item {} for {}ksh"
print(myorder.format(number, itemnum, price))

