#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words or enumerates a list of words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        print('You said: %s' % word)
        print('The word is %s' % word)
        print('')
    
<|/ file filename=word