
''' to make script executable'''
#executable #mode
$ chmod +x test.py     # This is to make file executable
$./test.py



#variables

A variable is created the moment you first assign a value to it.

Python allows you to assign values to multiple variables in one line

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

If you try to combine a string and a number, Python will give you an error:
x = 5
y = "John"
print(x + y)


#global variables
'''
Global Variables
Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
'''

def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)


Also, use the global keyword if you want to change a global variable inside a function.

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#data types

Python has five standard data types −

Numbers
String
List
Tuple
Dictionary

Python has the following data types built-in by default, in these categories:

Text Type:		str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:		set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview


You can get the data type of any object by using the type() function:

x = 5
print(type(x))


If you want to specify the data type, you can use the following constructor functions:


x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview


#data type conversions
#type conversios

int(x [,base]) 			- Converts x to an integer. base specifies the base if x is a string.
long(x [,base] ) 		- Converts x to a long integer. base specifies the base if x is a string.
float(x)				- Converts x to a floating-point number.
complex(real [,imag]) 	- Creates a complex number
str(x) 					- Converts object x to a string representation.

repr(x) 				- Converts object x to an expression string.
eval(str) 				- Evaluates a string and returns an object.

tuple(s) 				- Converts s to a tuple.
list(s) 				- Converts s to a list.
set(s) 					- Converts s to a set.	
dict(d) 				- Creates a dictionary. d must be a sequence of (key,value) tuples.
frozenset(s) 			- Converts s to a frozen set.
chr(x) 					- Converts an integer to a character.
unichr(x) 				- Converts an integer to a Unicode characte
ord(x) 					- Converts a single character to its integer value.
hex(x) 					- Converts an integer to a hexadecimal string.
oct(x) 					- Converts an integer to an octal string.


#bytes

x = b"Hello"	bytes

#bytearray
x = bytearray(5)	bytearray

#memoryview
x = memoryview(bytes(5))	memoryview

#set
x = {"apple", "banana", "cherry"}	set


#frozenset
x = frozenset({"apple", "banana", "cherry"})


#user input ---------------------------------
python user input

Python 3.6 uses the input() method.
Python 2.7 uses the raw_input() method.

Python 3.6
username = input("Enter username:")
print("Username is: " + username)

Python 2.7
username = raw_input("Enter username:")
print("Username is: " + username)

Python stops executing when it comes to the input() function, and continues when the user has given some input.


#slice operator
# slice operator ([ ] and [:] ) 
#string #strings ------------------------------------

'''
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
'''

#!/usr/bin/python

str = 'Hello World!'

print str          # Prints complete string
print str[0]       # Prints first character of the string
print str[2:5]     # Prints characters starting from 3rd to 5th
print str[2:]      # Prints string starting from 3rd character
print str * 2      # Prints string two times
print str + "TEST" # Prints concatenated string


#string #format #formating
python string formatting

Add a placeholder where you want to display the price:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

Format the price to be displayed as a number with two decimals:
txt = "The price is {:.2f} dollars"

If you want to use more values, just add more values to the format() method:
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


You can use index numbers (a number inside the curly brackets {0}) to be 
sure the values are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

You can also use named indexes by entering a name inside the curly brackets {carname}, 
but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

#collection ----------------


There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.



#lists #list

'''
To some extent, lists are similar to arrays in C. One difference between them is that all the items 
belonging to a list can be of different data type.
'''

#!/usr/bin/python

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd till 3rd 
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print list + tinylist # Prints concatenated lists


Range of negative indexes
This example returns the items from index -4 (included) to index -1 (excluded)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])



Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
#length
print(len(thislist))

#count
Return the number of times the value "cherry" appears int the fruits list:
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")


#add
'''add item'''

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

''' add item at specified index '''
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#remove
''' remove item from list'''
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


''' remove from specified index '''

The pop() method removes the specified index, (or the last item if index is not specified):

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


''' The del keyword removes the specified index: '''

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#clear #empty
''' The clear() method empties the list:'''
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#copy a list

You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, 
and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy().

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

Another way to make a copy is to use the built-in method list().

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Join Two Lists

There are several ways to join, or concatenate, two or more lists in Python.

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

Another way to join two lists are by appending all the items from list2 into list1, one by one:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

Or you can use the extend() method, which purpose is to add elements from one list to another list:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#list #constructor
It is also possible to use the list() constructor to make a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#tuples ----------------------

'''
The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and 
their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and 
cannot be updated. Tuples can be thought of as read-only lists. For example −
'''


#!/usr/bin/python

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print tuple           # Prints complete list
print tuple[0]        # Prints first element of the list
print tuple[1:3]      # Prints elements starting from 2nd till 3rd 
print tuple[2:]       # Prints elements starting from 3rd element
print tinytuple * 2   # Prints list two times
print tuple + tinytuple # Prints concatenated lists


Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, unless Python will not recognize the variable as a tuple.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

delete a tuple

Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exist


Search for the first occurrence of the value 8, and return its position:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)




#dictionaries

#!/usr/bin/python

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values

'''
Dictionaries have no concept of order among elements. It is incorrect 
to say that the elements are "out of order"; they are simply unordered.
'''

#bool

The bool() function allows you to evaluate any value, and give you True or False in return,

print(bool("Hello"))
print(bool(15))
will evaluate to True

Most Values are True
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.

Some values are false
In fact, there are not many values that evaluates to False, except empty values, such as (), [], {}, "", 
the number 0, and the value None. And of course the value False evaluates to False.

The following will return False

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


One more value, or object in this case, evaluates to False, and that is if you 
have an object that is made from a class with a __len__ function that returns 0 or False:

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

''' 
Python also has many built-in functions that returns a boolean value, 
like the isinstance() function, which can be used to determine
if an object is of a certain data type:
'''

x = 200
print(isinstance(x, int))

#numbers

#random numbers

Python does not have a random() function to make a random number, but Python has a 
built-in module called random that can be used to make random numbers:

import random
print(random.randrange(1,10))


#operators ---------

#floor division
floor division //
x = 15
y = 2

#the floor division // rounds the result down to the nearest whole number

print(x // y)

#exponention
x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2


#exception -----------------------
python try...except

The try block will generate an exception, because x is not defined:
try:
  print(x)
except:
  print("An exception occurred")


You can define as many exception blocks as you want, e.g. if you want to execute 
a special block of code for a special kind of error:


try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  
  
Try to open and write to a file that is not writable:

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
  
Raise an error and stop the program if x is lower than 0:
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")  

The raise keyword is used to raise an exception.
You can define what kind of error to raise, and the text to print to the user.

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
  
  
#function -------------------------

In Python a function is defined using the def keyword:
def my_function():
  print("Hello from a function")  
  

#arrays ---------------------------

Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.


#json ---------------------------

Python has a built-in package called json, which can be used to work with JSON data.

''' Convert from JSON to Python: '''

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


'''Convert from Python to JSON:'''

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)



''' Convert Python objects into JSON strings, and print the values:'''

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

'''When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:'''

Python	JSON
dict	Object
list	Array
tuple	Array
str		String
int		Number
float	Number
True	true
False	false
None	null


''' Convert a Python object containing all the legal data types: '''

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))


''' The json.dumps() method has parameters to make it easier to read the result: '''

Use the indent parameter to define the numbers of indents:

json.dumps(x, indent=4)

''' Use the separators parameter to change the default separator: '''

json.dumps(x, indent=4, separators=(". ", " = "))

''' Use the sort_keys parameter to specify if the result should be sorted or not: '''

json.dumps(x, indent=4, sort_keys=True)


#http #request
#urllib


from urllib.request import urlopen
from urllib.error import URLError
url = 'http://example.webscraping.com'
try:
html = urlopen(url).read()
except urllib2.URLError




#setup
#virtual environment
how to setup python virtual environment
Python Virtual Environments or Anaconda
The Conda introductory documentation (https://conda.io/docs/intro.html) is a good place to start!





#web scraping

Before diving into crawling a website, we should develop an understanding about the scale and
structure of our target website. The website itself can help us via the robots.txt and Sitemap files, and
there are also external tools available to provide further details such as Google Search and WHOIS.

example web site
http://example.webscraping.com/robots.txt: