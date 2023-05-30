#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words or prints a port. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            print('Bye!')
            break
        else:
            print('You said: ' + word)
            print('You said: ' + word + ' 