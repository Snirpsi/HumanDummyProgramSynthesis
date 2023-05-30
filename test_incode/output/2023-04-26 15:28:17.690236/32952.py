#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits or opens a list of words. """    
    while True:
        fruit = input('Enter a fruit or type "quit" to quit: ')
        if fruit == 'quit':
            break
        else:
            print('You entered ' + fru