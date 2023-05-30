#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print('You said: %s' % word)
            print('Now the program will repeat 