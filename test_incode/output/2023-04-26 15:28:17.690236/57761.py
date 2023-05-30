#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits or enumerates user input. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == 'quit':
            break
        else:
            print(