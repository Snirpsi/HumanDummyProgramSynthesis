#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports and opens a list of words. """    
    ports = range(1,65535)
    words = []
    
    while True:
        for port in ports:
            words.append(str(port*