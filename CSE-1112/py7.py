print("This is a program to count even and odd numbers in a list.")
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
print(list)
even_count = 0
odd_count = 0
for i in list:
    if i % 2 == 0:
        even_count+=1
    else:
        odd_count+=1
print("Odd numbers in the list is", odd_count)
print("Even numbers in the list is", even_count)