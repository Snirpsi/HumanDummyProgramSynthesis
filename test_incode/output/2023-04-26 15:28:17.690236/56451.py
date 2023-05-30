#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input. """    
    while True:
        answer = input('> ')
        if answer == 'quit':
            break
        print('You said "{}"'.format(answer))
