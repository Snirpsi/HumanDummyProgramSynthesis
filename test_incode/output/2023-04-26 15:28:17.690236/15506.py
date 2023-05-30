#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports and calculates a list of words. """    
    ports = range(1,65535)
    words = []
    for port in ports:
        words.append(str(port) + "