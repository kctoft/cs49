#!/usr/bin/env python
#
# If you are given 3 sticks, you may or may not be cable to arrange them in a triangle
# Ex. If one side is 12", and the other two are 1" long,
# you wont be able to get the short sticks to meet in the middle
#
# For any 3 lengths there is a test to prove if it's possible to make a triangle
# If any of these 3 lengths is greater than the sum of the other 2,
# it is NOT possible to make a triangle
# Otherwise you can
#
# This is a function called "is_triangle" that tests it for T/F

print("This is a program to test whether or not you have a triangle.")
print("Please answer the following questions.")

a = int(input("What is the length of the first side? '\n"))
b = int(input("What is the length of the second side?'\n"))
c = int(input("What is the legnth of the third side?'\n"))

def is_triangle(a, b, c):
    if a > (b + c):
        print("False, that will not work.")
    elif b > (a + c):
        print("False, that will not work.")
    elif c > (a + b):
        print("False, that will not work.")
    else:
        print("True, that is a triangle.")

print(is_triangle(a, b, c))
