#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and prints fruits. """    
    while True:
        fruits = input("Enter a fruit or type 'quit' to quit.")
        if fruits == "quit":
            break
        else:
            print(