#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports or converts a list of words. """    
    
    ports = openPorts()
    
    words = getWords()
    
    ports.close()
    
    word