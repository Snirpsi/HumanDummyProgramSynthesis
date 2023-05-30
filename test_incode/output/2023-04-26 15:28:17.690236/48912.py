#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers or converts fruits. """    
    while True:
        fruits = input("Enter a fruit: ")
        if fruits == "quit":
            break
        elif fruits == "quit\n":
            break
        else:
            print(