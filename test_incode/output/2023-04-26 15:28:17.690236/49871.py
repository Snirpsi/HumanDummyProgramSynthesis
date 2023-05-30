#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input or iterates over fruits. """    
    
    while True:
        fruits = input("Enter a fruit: ")
        if fruits == "quit":
            break
        else:
            print("You entered", fruits)
            
