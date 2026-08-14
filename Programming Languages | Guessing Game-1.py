# Programming Languages | Guessing Game
# Imani Candler | 9.1.2024
# Objective: Let the user guess a random number between 1 and 100. 
# Tell user if their guess is less than or more than the random number. Allow 10 guesses. 

import random
print ("Hi! Welcome to the Guessing Game! Guess a whole number between 0 and 100")

guess_number = random.randint(0,100)
# print (guess_number) had included this to test the random statement!
user_number = int(input("Enter your guess: "))

for n in range(10):
    if user_number < guess_number:
        user_number = int(input("Too low! Guess again: "))
        
    elif user_number > guess_number:
        user_number = int(input("Too high! Guess again: "))

    else:
        print()
        print ("You guessed it! The number was", guess_number) 
        break # break statement is important because it prevents the "else" statement from looping

if user_number != guess_number: # display statement if user can't guess the random number 
    print()
    print ("You lose! The number was", guess_number)


print ("Thanks for playing!")
