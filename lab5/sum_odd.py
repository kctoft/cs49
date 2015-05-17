#!/usr/bin/env python
#Lab 5, Question 2 (b)
#Q; Write a while loop fragment that calculates the following values...
# Sum of the first n odd numbers: 1+3+5+ ... + (2n - 1)

print("A program that finds out the sum of the first odd #'s: 1+3+5+...+n (2n -1)")
n = int(input("Enter a number for 'n': "))
def sum_odd(n):
    sum = 0
    i = 1
    while i <= n:
        sum = sum + ((2*i) - 1)
        i = i + 1
    print("The answer is: ")
    return sum

#tests
print(sum_odd(n))
