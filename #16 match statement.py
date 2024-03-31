a=int(input("Enter the number: "))
match a:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _ if a!=100:
        print("a is not 100")
    case _ if a==200:
        print("a is not 200")
    case _:
        print("a4 is:",a)