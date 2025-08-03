"""Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks."""

#Assign String to a Variable
#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
#Example
a = "Hello"
print(a)

'''Multiline Strings
You can assign a multiline string to a variable by using three quotes:

Example
You can use three double quotes:'''

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

'''Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.'''
#Example
#Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])
print(a[3])

'''Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.'''
#Example
#Loop through the letters in the word "banana":

for x in "banana":
  print(x)

'''String Length
To get the length of a string, use the len() function.'''
#Example
#The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))


'''Check String
To check if a certain phrase or character is present in a string, we can use the keyword in.'''

#Example
#Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

#Use it in an if statement:
#Example
#Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if NOT
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
#Example
#Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)
#Use it in an if statement:
#Example
#print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# more examples 
d ="dhanush is a good boy"
print ("is " in d )

d ="dhanush is a good boy"
print( 'lol' in d)

d ="dhanush is a good boy"
if "is" in d:
  print("yes")


d ="dhanush is a good boy"
if "lol" not in d:
  print("no")


"""Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string."""
#Example
#Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

d =" dhanush"
print(d[3:5])

'''Slice From the Start
By leaving out the start index, the range will start at the first character:'''
#Example
#Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

d =" dhanush"
print(d[:5])

'''Slice To the End
By leaving out the end index, the range will go to the end:'''
#Example
#Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])

d =" dhanush"
print(d[2:])

#Negative Indexing
#Use negative indexes to start the slice from the end of the string:
#Example
#Get the characters:

b = "Hello, World!"
print(b[-5:-2])

d =" dhanush"
print(d[-5:-1])

"""Python - Modify Strings
Python has a set of built-in methods that you can use on strings."""
#Upper Case
#ExampleGet your own Python Server
#The upper() method returns the string in upper case:

a = " Hello, World! "
print(a.upper())
#Lower Case
print(a.lower())
#Remove Whitespace
print(a.strip()) #removes the starting and end spaces
#Replace String
print(a.replace("H", "J"))


#Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


#Python - String Concatenation

#example-1
a = "Hello"
b = "World"
c = a + b
print(c)

#example-2
a = "Hello"
b = "World"
c = a + " " + b
print(c)

'''String Format
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:'''

#But we can combine strings and numbers by using f-strings or the format() method!

#F-Strings
#F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

#Example-1
#Create an f-string:
age = 36
txt = f"My name is John, I am {age}"
print(txt)
#Example-2
price = 59
txt = f"The price is {price} dollars"
print(txt)  #place holder

#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
#Example-1
#Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#Example-2
txt = f"The price is {20 * 59:.3f} dollars"
print(txt)

