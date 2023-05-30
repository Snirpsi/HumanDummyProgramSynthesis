#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or calculates user input. """    
    while True:
        fruit = input("Enter a fruit or type 'quit' to quit: ")
        if fruit == 'quit':
            break
        else:
            print(fruit)
