#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and calculates words. """    
    
    ports = range(1,65535)
    
    words = []
    
    for port in ports:
        words.append(str(port) + "