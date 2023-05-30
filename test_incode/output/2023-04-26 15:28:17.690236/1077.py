#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words and returns words. """    
    words = []
    while True:
        words.append(input('Enter a word: ').strip())
        if words:
            break
    print('The word 