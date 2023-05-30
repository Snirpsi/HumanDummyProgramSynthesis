#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words and adds all ports. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    words = []
    
    for port in ports:
        words.append(