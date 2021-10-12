print("This is a program to print all odd numbers in a range limit")
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
for i in range(start, end+1):
    if i % 2 != 0:
        print(i, end = " ")
