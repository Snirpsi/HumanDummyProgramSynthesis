#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words or adds user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = input('Enter a word: ')
    
    words = words.split()
    
    words.sort()
    
    print('\n'.join(words))
    
