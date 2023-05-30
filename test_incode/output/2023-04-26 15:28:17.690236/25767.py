#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a port and multiplyes a list of words. """    
    port = int(sys.argv[1])
    words = [x.strip() for x in open(sys.argv[2]).readlines()]
    
    words = [x.upper() for x in words]
    
    port = int(port)
    
    words = [