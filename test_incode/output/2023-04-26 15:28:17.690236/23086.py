#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and iterates over a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: '))
        if words == ['quit']:
            break
        else:
            print('You entered: ', words)
            print('The word 