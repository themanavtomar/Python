# there are four types of data types
# Data types are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data. Since everything is an object in Python programming, data types are classes and variables are instances (objects) of these classes.
# This code assigns variable ‘x’ different values of various data types in Python. It covers string, integer, float, complex, list, tuple, range, dictionary, set, frozenset, boolean, bytes, bytearray, memoryview, and the special value ‘None’ successively. Each assignment replaces the previous value, making ‘x’ take on the data type and value of the most recent assignment.
x = "Hello World"
x = 50
x = 60.5
x = 3j
x = ["geeks", "for", "geeks"] 
x = ("geeks", "for", "geeks") 
x = range(10) 
x = {"name": "Suraj", "age": 24} 
x = {"geeks", "for", "geeks"} 
x = frozenset({"geeks", "for", "geeks"}) 
x = True
x = b"Geeks"
x = bytearray(4) 
x = memoryview(bytes(6)) 
x = None
# Numeric Data Types in Python
# The numeric data type in Python represents the data that has a numeric value. A numeric value can be an integer, a floating number, or even a complex number. These values are defined as Python int, Python float, and Python complex classes in Python.
a = 5
print("Type of a: ", type(a)) 

b = 5.0
print("\nType of b: ", type(b)) 

c = 2 + 4j
print("\nType of c: ", type(c)) 
# Sequence Data Type in Python
# The sequence Data Type in Python is the ordered collection of similar or different data types. Sequences allow storing of multiple values in an organized and efficient fashion. There are several sequence types in Python –

# Python String
# Python List
# Python Tuple
# String Data Type
# Strings in Python are arrays of bytes representing Unicode characters. A string is a collection of one or more characters put in a single quote, double-quote, or triple-quote. In Python there is no character data type, a character is a string of length one. It is represented by str class.
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ") 
print(String1) 
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ") 
print(String1) 
print(type(String1)) 
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ") 
print(String1) 
print(type(String1)) 

String1 = '''Geeks 
			For 
			Life'''
print("\nCreating a multiline String: ") 
print(String1) 
# List Data Type
# Lists are just like arrays, declared in other languages which is an ordered collection of data. It is very flexible as the items in a list do not need to be of the same type.
List = [] 
print("Initial blank List: ") 
print(List) 
List = ['GeeksForGeeks'] 
print("\nList with the use of String: ") 
print(List) 
List = ["Geeks", "For", "Geeks"] 
print("\nList containing multiple values: ") 
print(List[0]) 
print(List[2]) 
List = [['Geeks', 'For'], ['Geeks']] 
print("\nMulti-Dimensional List: ") 
print(List) 
List = ["Geeks", "For", "Geeks"] 
print("Accessing element from the list") 
print(List[0]) 
print(List[2]) 
print("Accessing element using negative indexing") 
print(List[-1]) 
print(List[-3]) 
# Tuple Data Type
# Just like a list, a tuple is also an ordered collection of Python objects. The only difference between a tuple and a list is that tuples are immutable i.e. tuples cannot be modified after it is created. It is represented by a tuple class.
Tuple1 = () 
print("Initial empty Tuple: ") 
print(Tuple1) 
Tuple1 = ('Geeks', 'For') 
print("\nTuple with the use of String: ") 
print(Tuple1) 
list1 = [1, 2, 4, 5, 6] 
print("\nTuple using List: ") 
print(tuple(list1)) 
Tuple1 = tuple('Geeks') 
print("\nTuple with the use of function: ") 
print(Tuple1) 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('python', 'geek') 
Tuple3 = (Tuple1, Tuple2) 
print("\nTuple with nested tuples: ") 
print(Tuple3) 
tuple1 = tuple([1, 2, 3, 4, 5]) 
print("First element of tuple") 
print(tuple1[0]) 
print("\nLast element of tuple") 
print(tuple1[-1]) 
print("\nThird last element of tuple") 
print(tuple1[-3]) 
# Boolean Data Type in Python
# Data type with one of the two built-in values, True or False. Boolean objects that are equal to True are truthy (true), and those equal to False are falsy (false). However non-Boolean objects can be evaluated in a Boolean context as well and determined to be true or false. It is denoted by the class bool. 
print(type(True)) 
print(type(False)) 
print(type(True)) 
# Dictionary Data Type in Python
# A dictionary in Python is an unordered collection of data values, used to store data values like a map, unlike other Data Types that hold only a single value as an element, a Dictionary holds a key: value pair. Key-value is provided in the dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon : , whereas each key is separated by a ‘comma’.
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 
print("Accessing a element using key:") 
print(Dict['name']) 
print("Accessing a element using get:") 
print(Dict.get(3))