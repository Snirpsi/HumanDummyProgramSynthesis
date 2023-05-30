#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port and calculates a list of words. """    
    
    port = '/dev/ttyUSB0'
    
    words = []
    
    while True:
        
        words.append(