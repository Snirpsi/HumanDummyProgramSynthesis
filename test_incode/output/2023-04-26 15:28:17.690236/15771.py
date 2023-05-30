#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or converts fruits. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    if len(words) == 0:
        print('No words given')
        
    else:
        print('\n'.join(words))
        
