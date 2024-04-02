i=0
"""As the name suggests, while loops execute statements while 
the condition is True. As soon as the condition becomes False, 
the interpreter comes out of the while loop."""
while (i<=5):
    print(i)
    i=i+1
i=int(input("Enter the number:"))
while (i<8):
    print(i)
    i=i+1
print("this was done")
# decrementing while loop
i=10
while (i>0):
    print(i)
    i=i-1
else:
    print("your enter wrong")
# do while loop in python
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
# Example of a do-while loop in Python

# Initialize the condition to True
condition = True

# Execute the loop at least once
while condition:
    # Body of the loop
    print("This will always execute at least once.")

    # Ask the user if they want to continue
    user_input = input("Do you want to continue? (yes/no): ")

    # Check if the user wants to continue
    if user_input.lower() != 'yes':
        # If the user doesn't want to continue, set the condition to False to exit the loop
        condition = False
