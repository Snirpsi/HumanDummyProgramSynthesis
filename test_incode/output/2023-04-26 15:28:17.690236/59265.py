#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words and enumerates a port. """    
    port = '/dev/ttyUSB0'
    
    words = removeWords(port)
    
    for word in words:
        print(word)
    
    enumeratePorts(port)
    
