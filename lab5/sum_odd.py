#!/usr/bin/env python
#Lab 5, Question 2 (b)
#Q; Write a while loop fragment that calculates the following values...
# Sum of the first n odd numbers: 1+3+5+ ... + (2n - 1)

n = int(input("Enter a number for 'n': "))
def sum_odd(n):
    print("A program that finds out the sum of the first n odd #'s: 1+3+5+ ... +n")
    sum = 0
    i = 1
#    n = int(input("Please enter a number for 'n': "))
    while i <= n:
        sum = sum + ((2*i) - 1)
        i = i + 1
    print("The answer is: ")
    return sum

#tests
print(sum_odd(n))
