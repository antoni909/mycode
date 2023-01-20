#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

"""Below is a script for a number guessing game! However, it's busted! Please try 
and get it operational (no need to improve it, just make it work).

When working properly, the user should have 5 chances to guess a number that is 
between 1 and 100. The program will tell the user if they guess too high or too low, 
and if they guess correctly the script should end! """

# fix-1: added missing import
import random

def main():
    
    num = random.randint(1,100)
    rounds = 0
    # fix-2: initialize guess to empty string
    guess = ""

    while rounds < 10 and guess != num:
        

        guess = input("Guess a number between 1 and 100\n>")
        guess = int(guess)
        
        # fix-3: add += to update rounds value
        if guess > num:
            print("Too high!")
            rounds += 1
        # fix-4: add += to update rounds value
        elif guess < num:
            print("Too low!")
            rounds += 1
        # fix-5: break out of loop if correct guess
        else:
            print("Correct!")
            break

#fix-6: call main functon
if __name__ == "__main__":
    main()
