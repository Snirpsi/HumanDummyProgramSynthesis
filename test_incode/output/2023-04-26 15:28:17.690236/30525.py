#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words or converts fruits. """    
    while True:
        fruits = input("Enter a fruit or type 'quit' to exit: ")
        if fruits == 'quit':
            break
        else:
            print(