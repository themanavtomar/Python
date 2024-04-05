txt = "For only {price:.2f} dollars!" #2f means two digits after decimal we also can say that float of 2 digit
print(txt.format(price = 49.551))
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"
print(letter.format(country, name))
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Harry"
print(letter.format(country, name)) #to solve this problem we use f-string
#thats why we use f-strings in python
val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  
name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")
print(f"{2 * 30}")