#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or prints fruits. """    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'quit':
            break
        else:
            print(