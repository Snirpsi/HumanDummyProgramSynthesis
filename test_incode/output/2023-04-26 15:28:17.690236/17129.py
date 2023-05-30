#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a port or removes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
        
        if port == 'remove':
            remove_words()
        else:
            store_words()
    else:
        print('Usage: python ports.py [port]')
        
