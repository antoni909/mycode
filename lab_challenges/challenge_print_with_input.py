#!/usr/bin/env python3

"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():

    # collect string input from the user
    user_name = input("Please enter your name")
    user_date = input("Please enter current day of the week")
    
    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("Hello," + user_name +"! Happy " + user_date + "!")

main()


