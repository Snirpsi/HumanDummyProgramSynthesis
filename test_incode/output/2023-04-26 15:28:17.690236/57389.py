#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port and converts a list of words. """    
    port = int(sys.argv[1])
    words = sys.argv[2:]
    
    remove_port(port, words)
    
