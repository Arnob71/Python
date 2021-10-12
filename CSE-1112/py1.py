print("This is a program to calculate the area of a triangle")
print("The value of 1st,2nd and 3rd side of the triangle is 5,6 and 7")
a = 5
b = 6
c = 7
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is %0.2f" %area)