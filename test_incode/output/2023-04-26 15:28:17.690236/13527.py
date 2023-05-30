#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input or stores fruits. """    
    while True:
        fruits = input('Enter a fruit (type "quit" to quit): ')
        if fruits == 'quit':
            break
        else:
            print('You entered', fruits)
