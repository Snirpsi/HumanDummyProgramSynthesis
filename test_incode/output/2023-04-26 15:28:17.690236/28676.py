#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or removes fruits. """    
    while True:
        fruits = input("Enter fruits: ")
        if fruits == 'exit':
            break
        else:
            print(