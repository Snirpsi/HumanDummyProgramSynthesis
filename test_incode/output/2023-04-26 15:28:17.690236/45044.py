#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words or returns a port. """    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            print('Goodbye!')
            break
        else:
            print('You said: ' + word)
            