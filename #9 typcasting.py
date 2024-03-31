# Write typecasting
# The conversion of one data type into the another data type is known as type casting in python or type conversion in python.
# python supports a wide variety of functions or methods likes int(),Float(),Str(),ord(),tuple(),set(),list,dict,Etc 4 type casting in python.
# There are two types of typecasting
# 1.explicit conversion(explict type costing in python)
# Python program to demonstrate explicit conversion
# int variable
a = 5.9

# typecast to int
n = int(a)

print(n)
print(type(n))

# int variable
a = 5

# typecast to float
x = float(a)

print(x)
print(type(x))
# 2.Implicit conversion(Implicit type casting in python)
# Python program to demonstrate 
# implicit type Casting 

# Python automatically converts 
# a to int 
a = 7
print(type(a)) 

# Python automatically converts 
# b to float 
b = 3.0
print(type(b)) 

# Python automatically converts 
# c to float as it is a float addition 
c = a + b 
print(c) 
print(type(c))

# Python automatically converts 
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))

