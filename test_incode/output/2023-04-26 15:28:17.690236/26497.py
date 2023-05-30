#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input or iterates over fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == 'quit':
            break
        else:
            fruit