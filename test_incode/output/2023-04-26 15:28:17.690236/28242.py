#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words or multiplyes a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
    
    for word in enumerate(''.join(sys.argv[2:])):
        print('{} * {}'.format(word, port