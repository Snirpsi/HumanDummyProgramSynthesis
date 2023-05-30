#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'words.txt'
    
    with open(filename) as f:
        words = [word.strip() for word in f.readlines()]
    
    print('\n'.join(words))
    
