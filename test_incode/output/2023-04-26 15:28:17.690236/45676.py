#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or converts fruits. """    
    while True:
        fruits = input("Enter a fruit: ")
        if fruits == 'quit':
            break
        else:
            print(