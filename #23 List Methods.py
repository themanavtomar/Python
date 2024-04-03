colors=["voilet","indigo","blue","green"]
colors.sort()
print(colors)
num=[5,2,4,1,6,8,7,6,5]
num.sort()
print(num)
#for reverse
num=[5,2,4,1,6,8,7,6,5]
num.sort(reverse=True)
print(num)
#reverse the simple list according to their order
num=[1,2,3,4,5,6,7,8]
num.reverse()
print(num)
#index
colors = ["voilet","indigo","blue","green"]
print(colors.index("indigo"))
#count how many time element repeate
c=["a","a","a","a","b","c","d","e","f","f","f","g"]
print(c.count("a"))
#copy
#why we use copy
#problem
l=[11,45,1,2,4,6,1,1]
print(l)
m=l
m[1]=12
print(l)
#copy main use
a=["a","a","a","a","b","c","d","e","f"]
newlist=a.copy()
print("this is newlist before changes=",newlist)
newlist[0]=2
newlist[1]=4
print(newlist)
print("a is always same=",a)
#append()
colors=["voilet","indigo","blue"]
colors.append("green")
print(colors)
#insert()
colors=["voilet","indigo","blue"]
colors.insert(2,"green")
#extend()
colors=["voilet","indigo","blue"]
rainbow=["green","yellow","orange","red"]
colors.extend(rainbow)
print(colors)
#we can concatenating two list
color1=["yellow","indigo","blue","green"]
color2=["voilet","orange","red"]
print(color1+color2)
