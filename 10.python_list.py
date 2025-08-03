#Python Lists
mylist = ["apple", "banana", "cherry"]
'''List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:'''

#Example
#Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)
#List Items
'''List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.'''

#Ordered
'''When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.'''
#Allow Duplicates
'''Since lists are indexed, lists can have items with the same value:'''

#Example
#Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))

'''List Items - Data Types
List items can be of any data type:'''

#Example
#String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A List Contain different Data types 
#Example
list1 = ["abc", 34, True, 40, "male"]

#type()
#From Python's perspective, lists are defined as objects with the data type 'list':

print(type(list1))

#list() constructor
#Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
"""
Access Items
List items are indexed and you can access them by referring to the index number:
"""

#Example
#Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

'''
Negative Indexing
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.
'''
#Example
#Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# changing the list values
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry"]
thislist[1:3] =[ "blackcurrant","grapes"]
print(thislist)

#Example
#Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert Items
#Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#adding list items
#append()
thislist = ["apple", "banana", "cherry"]
thislist.append("grapes")
print(thislist)

a =["apple", "orange","grapes"]
b= ["mango","guava",12]
a.extend(b)
print(a)

a.remove("apple")
print(a)
a.pop(4)
print(a)

#delete list
thislist = ["apple", "banana", "cherry"]
del thislist[0] #or use (del thislist) to delete complete list 
print(thislist)

#clear the list 
a= ["appl","orange"]
a.clear()
print(a)

# Loop Lists
#You can loop through the list items by using a for loop:
#Ecample
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

a=[1,2,3,4,5]
for i in range(len(a)):
  print(a[i])  

#using while loop 
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1  

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x: #in append the items to newlist which having a in the fruits
    newlist.append(x)

print(newlist)  

'''
or use newlist = [x for x in fruits "a" in x]
print(new list)
'''

# use newlist

a = ["banana","mango","apple","aaple"]

b = [x for x in a if x != "apple"]
print(b)
b = [x for x in a if x != "mango"]
print(b)
b=a
print(b)
c = [x for x in range(10)]
print(c)

d = [x for x in range(10) if x >=5]
print(d)

e = ["hello " for x in d]

print(e)

f= [ x if x != "apple" else "grapes" for x in a]
print(f)
#Sort List Alphanumerically
a.sort()
print(a)

s=[10,23,3,6,87,]
s.sort()
print(s)

s.sort(reverse= True )
print(s)

#repalce
mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[3])  