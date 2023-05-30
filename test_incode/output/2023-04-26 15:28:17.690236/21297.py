#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words or prints a list of numbers. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    words.sort()
    numbers.sort()
    
    print('\n'.join(map(str, words)))
    print('\n'.join(map(str, numbers)))
    
