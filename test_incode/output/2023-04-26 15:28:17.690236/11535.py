#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words and enumerates a port. """    
    words = []
    ports = range(1,65535)
    for port in ports:
        words.append(str(port))
    
    words.sort()
    
    word