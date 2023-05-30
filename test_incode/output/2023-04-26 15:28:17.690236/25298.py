#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words. """    
    while True:
        word = str(input('Enter a word: '))
        multiplier = 1
        for char in word:
            multiplier = multiplier * int(char)
        print('The word multiplied by %d is %s.' % (multiplier, word))
