#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words and returns a list of numbers. """    
    words = ['cat', 'dog', 'mouse', 'rabbit', 'monkey']
    numbers = []
    for word in words:
        numbers.append(word.count('