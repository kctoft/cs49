#!/usr/bin/env python
# Lab 5, Question 2 (a)
# Q: write a while loop fragment that calculates the following values...
# (a) Sum of the first n countring numbers: 1 + 2 + 3 + ... + n

print("A program that finds the sum of 1+2+3 ... +n")
n = int(input("Please enter a value for 'n': "))
def sum_counting(n): #takes the parameter 'n'
    sum = 0 #declare the variable
    i = 1 #ensures the value for n remains unchanged
    while i <=  n:
        sum = sum + i
        i = i + 1
    print("The answer is:")
    return sum #returns the new value for 'sum'

#tests
print(sum_counting(n))
