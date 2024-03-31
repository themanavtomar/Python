a="manav"
print(a.upper())
b="MANAV"
print(b.lower())
c="Manav don!!! !!!!"
d="    'Manav don!!! !!!!!!' "
print(b.casefold())
print(d.strip())
print(c.rstrip("!"))#remove the particular character
print(c.replace("don","Tomar"))#replace the word
print(c.split(" "))#split from which we give in command
print(a.capitalize()) ##capital first letter of word.
srt1="welcome to my console"
print(len(srt1))
print(len(srt1.center(50)))#takes total index from starting
print(c.count("!"))#count the string comes how many time 
d="my name is manav"
print(len(d))
print(d.endswith("manav")) #tells end with which word
d="my name is manav"
print(d.endswith("is",0,10)) #is tells that particular word ends with that or not
print(d.find("manav"))
print(d.index("manav"))
e = "mynameismanav"
print(e.isalnum())
print(d.islower())
print(d.isprintable())
f = '           '
print(f.isspace())
