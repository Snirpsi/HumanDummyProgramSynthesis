#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        print(' '.join(word.split()))
        
    else:
        print('Usage: {} word'.format(sys.argv[0]))
        
