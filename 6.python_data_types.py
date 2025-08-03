"""Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:"""
 
#Text Type:	      str
#Example
x = "Hello World"
#Numeric Types:	  int, float, complex

x = 20	#int	
x = 20.5	#float	
x = 1j    #complex
##Sequence Types:   list, tuple, range
#Example
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range

#Mapping Type:	  dict
#Example
x = {"name" : "John", "age" : 36}

#Set Types:	      set, frozenset
#Example
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset
#Boolean Type:	  bool
#Example
x = True
#Binary Types:	  bytes, bytearray, memoryview
#Example
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview
#None Type:	      NoneType
#Example
x = None	#NoneType