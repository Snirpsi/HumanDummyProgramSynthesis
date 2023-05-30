#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['cat', 'dog', 'bird', 'snake', 'monkey', 'lion', 'tiger']
    
    for word in words:
        print('{} is a {}'.format(word, word.isupper()))
    
    print('\nPress CTRL+C to exit')
    
    