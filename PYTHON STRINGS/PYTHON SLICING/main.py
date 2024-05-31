# slicing is the process of returnig range of character
#Specify the start index and the end index, separated by a colon, to return a part of the string.
#EXAMPLE
 
b="hell0 word"
print(b[2:5])
# this prints llo since it returns eleent at index 2 to 4
#note that index 5 is excluded


# sliceing from start
# we leave the first index but specify the index at which it will stop slicing
# EXAMPLE
b = "helllo word"

print(b[:5])

# we can also slice at the end of a string
b = "hello word"
print(b[2:]) #this prints from index 2 to the end''


# negative indexing
# Use negative indexes to start the slice from the end of the string:

"""Example
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):

"""

b = "Hello, World!"
print(b[-5:-2])