#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words. """    
    words = ['cat', 'dog', 'bird', 'snake', 'mouse']
    
    while True:
        words.append(input('Enter a word: '))
        
        print('The word was:', 