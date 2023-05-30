#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words and prints words. """    
    words = []
    while True:
        words.append(input('Enter a word: '))
        print('You entered', words)
        print('You said', end=' ')
        print(' '.join(words))
        print('')
        print('Press ENTER to quit.')
