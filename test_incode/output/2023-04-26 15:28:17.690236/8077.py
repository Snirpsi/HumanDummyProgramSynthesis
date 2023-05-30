#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input or calculates numbers. """    
    
    number = input("Enter a number: ")
    
    if number == "quit":
        print("Goodbye!")
        exit()
    
    if number == "add":
        print("The sum of two numbers is " + str(