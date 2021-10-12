print("This is a program to find the factorial of a number")
num = int(input("Enter the number: "))
factorial = 1
if num<0:
    print("Factorial doesn't exist for negative numbers")
else:
    for i in range(1, num+1 ):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)