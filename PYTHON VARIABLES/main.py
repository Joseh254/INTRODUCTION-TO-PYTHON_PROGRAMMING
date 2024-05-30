# variables are containers for storing data
"""Creating Variables

Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it or initialize it.

Example"""

my_name = "joseph"  #assigning a string 'joseph' to variable named my_name

x = 57 # assigning an integer datatype

xyz = True

# variables can be changed 
# example

y = 4
y = 10

print(y)

# this will print 10 in terminal


# *********************************EXERCISE************************************************
# you can specify the datatype as shown below

name = str('joseph mbugua')
print(name)

# will print joseph mbugua

#  Python is case sensitive.That mean a = 5 is not the same as A =54

a= 5
A = 45

print(a) #will print 5 in the terminal

print(A)# will print 45 in terminal


# PYTHON VARIABLE NAMES
# RULES FOR NAMING A VARIABLE

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

"""

"""
you can declare multiple variables in single statement

"""

name,age,gender = "joseph",25,"male"
print(age)
print(gender)
print(name)


"""One Value to Multiple Variables

And you can assign the same value to multiple variables in one line:

Example
"""
my_favourite_color = my_dad_favourite_color = my_son_favourite_color = str('Black')
print(my_favourite_color) #print black
print(my_dad_favourite_color)#print black
print(my_son_favourite_color)# print black


#PRINTING MULTIPLE ITEMS

A = 5
c =8
f =10

print(A,c,f) #this will print 5,8 and 10 in the terminal


#***********************GLOBAL VARIABLES*****************************8

# Global variables are variables that are accesible in entire code
#the are declared otside a function and they can be used inside the fuctions

# EXAMPLE
x = "easy"

def myfunction():
  print("Python is " + x)

myfunction()

"""
The global Keyword

When you create a variable inside a function, that variable is local variable, and can only be used inside that function or block.

To create a global variables inside a function, you can use the global keyword.
"""

def example():
  global y
  y ="joseph"


def runExample():
  print(y)

runExample() #this will print the value of y which is the string joseph




# WRITE A PROGRAM IN PYTHON TO ADD TWO NUMBERS.USE  COMMENTS TO DOCUMENT YOUR WORK