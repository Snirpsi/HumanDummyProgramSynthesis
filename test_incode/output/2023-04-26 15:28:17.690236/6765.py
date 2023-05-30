#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers or removes a list of words. """    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        if arg == '--words':
            words = sys.argv[2:]
            break
    
    words = list(set(words))
    
    if len(words) == 0:
        print('No words given.')
        sys.exit()
    
    words.sort()
    
    print('\n'.join(words))
    
    
