#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words and prints a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: '))
        if words:
            print(', '.join(words))
        else:
            break
