#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input and returns fruits. """    
    while True:
        fruit = input("Enter a fruit (apple, orange, pear, etc.): ")
        if fruit == "quit":
            break
        else:
            print(