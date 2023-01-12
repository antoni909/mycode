#!/usr/bin/env python3
import random
def main():
    """runtime function"""
    choices = {
        0 : "rock",
        1 : "paper",
        2 : "scissors" 
    }
    round = 1
    wins = 0
    lost = 0
    draws = 0
    play_again = True

    while( play_again ):
        print(f"\nROUND: {round}    W: {wins}   L: {lost}   D: {draws} ")
        user_choice = input("    Please Type One: rock, paper, scissors OR q to exit \n")
        user_choice = user_choice.lower()
        random_idx = random.randint(0,2)
        random_choice = choices[random_idx]

        print(f"    YOU: {user_choice}     Computer: {random_choice} ")
        # Handle User Input Rock
        if user_choice == "rock":
            if random_choice == "paper":
                print(f"    YOU LOST {random_choice} beats {user_choice} \n")
                lost += 1
            elif random_choice == "scissors":
                print(f"    YOU WON {user_choice} beats {random_choice} \n")
                wins += 1
            else:
                print(f"    ITS A DRAW {user_choice} - {random_choice} \n")
                draws += 1
        if user_choice == "paper":
            if random_choice == "rock":
                print(f"    YOU LOST {random_choice} beats {user_choice} \n")
                lost += 1
            elif random_choice == "scissors":
                print(f"    YOU WON {user_choice} beats {random_choice} \n")
                wins += 1
            else:
                print(f"    ITS A DRAW {user_choice} - {random_choice} \n")
                draws += 1
        if user_choice == "scissors":
            if random_choice == "rock":
                print(f"    YOU LOST {random_choice} beats {user_choice} \n")
                lost += 1
            elif random_choice == "paper":
                print(f"    YOU WON {user_choice} beats {random_choice} \n")
                wins += 1
            else:
                print(f"    ITS A DRAW {user_choice} - {random_choice} \n")
                draws += 1
        
        # Handle Exit
        if user_choice == "q":
            play_again = False
            print("\nThanks for playing")

        round += 1

# call our main function
if __name__ == "__main__":
    main()
