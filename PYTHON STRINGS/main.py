# ******************************************PYTHON STRINGS****************************************

# Strings are sequence of character sand they are sorounded by either single or double quotes
# 'joseph' is the same as "joseph"

my_name = "joseph"
myName = 'joseph'

print(my_name)

print(myName)

# they both return joseph
# #ASSIGNING STRING TO VARIABLE
#we use an equal operator to assign string to variabkes

a = "this is a string"

# ******************MULTIPLELINE STRINGS******************
a = """
my 
favourite 
movie 
is 
Agent x

"""
# for this case we use either three single or double quotes

print(a)

#someone can be right to say strings are arrays and for this case square brackets ae used
#to access elements of the string.

a = "hello world"
print(a[0]) #returns the first character in the string which id h
#elements starts from index 0


#*************************LOOPING THROUGH STRING*****************
#Since strings are arrays, we can loop through the characters in a string, with a for loop.

for i in "I miss her":(j)

print(j) #returns all the elements of the string


# ****************LENGTH OF A  STRING*********************
# to get the length of the string we use  keyword len

a = 'hello'
print(len(a)) 


#******************CHECKING IF A CHARACTER OR PHRASE EXISTS IN A STRING****************
#We use keyword in as shown below
text = "Serving Christ is a good decision"
print("Christ" in text)

#we can also use conditional statements to check

text = "serving Christ is a wise decision"
if "wise" in text:
    print("wise exists in the string")

    #we will learn more on conditional statements later


    # CHECK IF A STRING OR PHRASE IS NOT PRESENT
    #we use keyword not in
    # example

