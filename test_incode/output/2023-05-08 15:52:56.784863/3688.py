#!/usr/bin/python3
if __name__ == '__main__':
    #A program that converts user input.
    #This program will take user input from the command line
    #and convert it to a number.
    #The program will then print out the number the user entered.
    #The program will then ask the user if they would like to continue.
    #If the user enters yes, it will continue to ask the user if they would like to continue.
    #If the user enters no, it will exit the program.
    import sys
    number = int(sys.argv[1])
    answer = input("Would you like to continue (y/n)? ")
    if answer == "y":
        print("The number you entered is", number)
    elif answer == "n":
        sys.exit()

