#!/usr/bin/env python
# lab 4
# Q 4.3
#
# Write a program that 1st generates a random integer between 0 && 100
# Tthen pass that number to a fcn to prompt the user to guess what it is
# Once the number is found, return the total number of guesses
# In the main fcn, print out the # && # of tries it took

import random

secret_number = random.randint(0,100) #returns random int such that a <= x <= b
guess = int(input("Please enter your guesss: "))

def guessing_game(secret_number, guess):
    print("Play a game with me.\n")
    print("The computer generated a number for you.")
    print("I am guessing a number between 0 and 100.\n")
    secret_number = random.randint(0,100)
    guess = int(input("Please enter your guess:(<Enter> to quit) >> ")) #user input
    tries = 1
    print("My secret number is ", secret_number)
    while (True): #continueous loop
        if (guess > secret_number): #guess is bigger than the number
            print("Your guess is greater than the secret number, try again.")
        elif (guess < secret_number):
            print("Your guess is less than the secret number, try again.")
        else:
            print("Congradulations, you guessed right!")
            print("The secret number was ", secret_number, " and you have made ", tries, " guesses. \n")
            break
        guess = int(input("Please try a different number: "))

print(guessing_game(secret_number, guess))
