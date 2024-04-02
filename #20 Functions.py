"""A function is a block of code that performs a specific task whenever it is called. 
In bigger programs, where we have large amounts of code, it is advisable to create or use existing 
functions that make the program flow organized and neat.

There are two types of functions:
1.Built-in functions
2.User-defined functions
Built-in functions:
These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:
min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

User-defined functions:
We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions."""
def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)
c=4
d=4
calculateGmean(c, d)
def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass
  

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)
#now we create our own function where we can ,ake a function for addition.
def Addition(a,b,c,d,e,f):
  sum=(a+b+c+d+e+f)/2
  print(sum)
a=2
b=3
c=4
d=5
e=6
f=7
Addition(a,b,c,d,e,f)