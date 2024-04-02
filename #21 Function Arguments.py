#Function Arguments and return statement
#1.Default arguments:
"""We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument."""
#Example:
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)
name("Manav","Tomar","Jaat")
name("Don")

#2.Keyword arguments:
"""We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter."""
#Example:
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name(mname = "Manav", lname = "Tomar", fname = "Jaat")

#3.Required arguments:
"""In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition."""
#Example:
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Manav", "","Tomar")

#4.Variable-length arguments:
"""Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments."""
#There are two ways to achieve this:
    #1.Arbitrary Arguments:
"""While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple."""
#Example:
def name(*name):
    print("Hello,", name[0], name[1], name[2])
name("Manav", "Tomar", "Jaat")

    #2.Keyword Arbitrary Arguments:
"""While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary."""
#Example:
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "Tomar", lname = "Jaat", fname = "Manav")

#Return Statement
"""The return statement is used to return the value of the expression back to the calling function."""
#Example:

def name(fname, mname, lname):
    return "Hello," + fname + " " + mname + " " + lname
print(name("Manav", "Tomar", "Jaat"))

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)
c = average(7.09, 5.74, 6.2, 6.88,7.5,8.59)
print(c)