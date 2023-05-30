#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input or returns user input. """    
    while True:
        answer = input('> ')
        if answer == 'exit':
            break
        else:
            print('You said ' + answer)
