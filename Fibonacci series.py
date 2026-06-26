a = int(input("a "))
b = int(input("b "))
n = int(input("Enter the terms of  Fibonacci series"))
for i in range(n):
    print(a)
    temp = a+b
    a = b
    b = temp

