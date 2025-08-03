#python - Variable Names
'''Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
ExampleGet your own Python Server
Legal variable names:'''

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Example
#Illegal variable names:
'''2myvar = "John"
   my-var = "John"
   my var = "John"'''


#Multi Words Variable Names
#Variable names with more than one word can be difficult to read.

#There are several techniques you can use to make them more readable:

#Camel Case
#Each word, except the first, starts with a capital letter:

myVariableName = "John"
#Pascal Case
#Each word starts with a capital letter:

MyVariableName = "John"
#Snake Case
#Each word is separated by an underscore character:

my_variable_name = "John"

'''Python Variables - Assign Multiple Values
Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:'''

#Example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

'''One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:'''
#Example
x = y = z = "Orange"
print(x)
print(y)
print(z)

'''Python - Output Variables
Output Variables
The Python print() function is often used to output variables.'''

#Example
x = "Python is awesome"
print(x)

#In the print() function, you output multiple variables, separated by a comma:
#Example
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#You can also use the + operator to output multiple variables:
#Example
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
#For numbers, the + character works as a mathematical operator:
#Example
x = 5
y = 10
print(x + y)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
#Example
'''x = 5
   y = "John"
   print(x + y)'''

#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
#Example
x = 5
y = "John"
print(x, y)

