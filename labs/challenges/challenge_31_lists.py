#!/usr/bin/env python3
import random

def main():

    wordbank= ["indentation", "spaces"] 
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 
                  'Craig', 'Deja', 'Elihu', 'Eric', 
                  'Giovanni', 'James', 'Joshua', 'Maria', 
                  'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 
                  'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    # PART 3. Add a line of code that appends the integer 4 to the list wordbank.
    wordbank.append(4)

    # Include an input asking for a number between 0 and 20. Save this as the variable num.
    num = input("pick a number between 0 and 20")
    # convert num into an integer!
    num = int(num)

    # Use the integer num to slice one of the elements from the list tlgstudents. Save the name you return as the variable student_name.
    student_name = tlgstudents[num]
    print(student_name, "always uses ",wordbank[2], wordbank[1], " to indent. ")


    # for Bonus 1 Find a way to randomize what student name is picked
    name = random.choice(tlgstudents)
    print(name, "always uses ",wordbank[2], wordbank[1], " to indent. ")


if __name__ == "__main__":
    main()
