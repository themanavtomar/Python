#python list
list=[1,2,3,4,5,6]
print(list)
print(type(list))
l=[1,"manav",2,"tomar"]
print(l)
#list index
color=["red","blue","yellow","green"]
print(color[2])
#negative indexing
color=["red","blue","yellow","green"]
print(color[-2])
print(color[len(color)-2])#converting it into postive indexing
print(color[4-2])#converting it into postive indexing
if "yellow" in color:
    print("this is yellow color")
else:
    print("color is absent")
#range of index
color=["red","blue","yellow","green","black","orange","black","white"]
print(len(color))
print(color[2:7])
print(color[:])
print(color[-8:])
#and many more ways 
#printing altenative values
color=["red","blue","yellow","green","black","orange","black","white"]
print(color[1: :2])
#list comparision 
color=["red","blue","yellow","green","black","orange","black","white"]
colorWith_0=[item for item in color if "b" in item]
print(colorWith_0)
color=[item for item in color if (len(item)>5)]
print(color)