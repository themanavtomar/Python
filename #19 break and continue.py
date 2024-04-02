for i in range(12):
    if i==10:
       break
    print("5 X", i+1, "=", 5 *(i+1))
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    """else:
       print("Mississippi")"""
print("Thank you")
for i in [2,3,4,6,8,10]:
    if (i%2!=0):
        continue
    print(i)