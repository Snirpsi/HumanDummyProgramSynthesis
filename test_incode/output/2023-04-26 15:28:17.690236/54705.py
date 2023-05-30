#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words. """    
    words = []
    while True:
        words.append(input('Enter a word: ').strip().lower())
        if words[-1] == 'q':
            break
    print('\n'.join(words))
