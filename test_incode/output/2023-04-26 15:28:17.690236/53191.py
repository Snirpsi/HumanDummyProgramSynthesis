#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    import sys
    
    if len(sys.argv) != 2:
        sys.exit('Usage: python wordserver.py <word>')
    
    word = sys.argv[1]
    
    print('Adding 