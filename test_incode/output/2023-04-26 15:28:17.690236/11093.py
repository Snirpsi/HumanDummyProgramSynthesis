#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of numbers and enumerates words. """    
    numbers = list(range(1,101))
    words = list(enumerate(' '.join(numbers)))
    print(words)
    
