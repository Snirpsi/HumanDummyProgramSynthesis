#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits or converts a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        fruit = sys.argv[1]
    else:
        fruit = 'apple'
    
    words = [fruit + ' ' + w for w in 'banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana banana 