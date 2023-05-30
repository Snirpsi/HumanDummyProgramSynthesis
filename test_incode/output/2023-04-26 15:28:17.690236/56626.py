#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words or converts fruits. """    
    while True:
        fruits = input("Enter fruits: ")
        if fruits == 'exit':
            break
        else:
            words = fru