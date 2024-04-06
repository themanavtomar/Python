#factorial
def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code 
num = 7; 
print("Number: ",num)
print("Factorial: ",factorial(num))

#fibonacci series
def fib(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    print("The first 10 Fibonacci numbers are:")
    for i in range(int(input("enter your number:"))):
        print(fib(i))
    else:
        print("please dont enter zero")
if __name__ == "__main__":
    main()