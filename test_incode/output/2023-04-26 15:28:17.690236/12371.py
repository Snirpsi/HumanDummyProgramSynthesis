#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports and converts a list of words. """    
    ports = openPorts()
    words = convertWords(ports)
    print(words)
    
