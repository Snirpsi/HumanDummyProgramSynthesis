#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words or enumerates words. """    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        print(word)
        
    if len(words) == 0:
        print('No words given.')
    else:
        print('Words:')
        for word in words:
            print(word)
        
    print('Done.')
    
