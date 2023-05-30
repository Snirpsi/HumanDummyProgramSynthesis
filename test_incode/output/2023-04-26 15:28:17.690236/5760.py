#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits or enumerates user input. """    
    while True:
        print("Type 'quit' to quit")
        fruit = input("Enter a fruit: ")
        if fruit == 'quit':
            break
        else:
            print(