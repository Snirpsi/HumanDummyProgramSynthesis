#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: ').strip())
        if words == ['quit']:
            break
        print('The word 