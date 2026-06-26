a = 0
b = 1
n = int(input("Enter the terms of  Fibonacci series"))
for i in range(n):
    print(a)
    temp = a+b
    a = b
    b = temp

