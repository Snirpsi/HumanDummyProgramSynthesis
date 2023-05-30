#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input or calculates a list of words. """    
    
    words = []
    while True:
        words.append(input('Enter a word: '))
        if words[-1] == 'quit':
            break
        else:
            print('The word is', end=' ')
            print(words[-1])
            print('