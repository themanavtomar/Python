fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
print(fruit[0:4]) # including 0 but not 4
print(fruit[1:4]) # including 1 but not 4
print(fruit[:5])
print(fruit[0:-3])
print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])
pie = "ApplePie"
print(pie[:5])
print(pie[6])	#returns character at specified index
alphabets = "ABCDE"
for i in alphabets:
    print(i)
nm = "Harry"
print(nm[-4:-2])