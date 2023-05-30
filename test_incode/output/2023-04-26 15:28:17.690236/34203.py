#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input. """    
    while True:
        answer = input('> ')
        if answer == 'quit':
            break
        elif answer == 'add':
            print('You entered "add"')
        else:
            print('You entered "quit"')
