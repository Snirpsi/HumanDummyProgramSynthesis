#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input. """    
    while True:
        answer = input('> ')
        if answer == 'q':
            break
        else:
            print('Invalid input')
