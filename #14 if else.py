# if-else Statements
# Based on this, the conditional statements are further classified into following types:
# if
a = int(input("Enter your age: "))
print("Your age is:", a)
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)
if(a>=18):
  print("You can drive")
  print("Yes")
else:
  print("You cannot drive")
  print("No")
  print("Yay!")
# if-else
applePrice = int(input("Current Apple Prize is:"))
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")
# if-else-elif
num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")
print("I am happy now")
# nested if-else-elif.
num = int(input("Enter the number: "))
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
print("Thanks for using this code hats off!")
# # Conditional operators 
# # >, <, >=, <=, ==, !=
