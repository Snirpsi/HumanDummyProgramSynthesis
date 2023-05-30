#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words and converts all ports. """    
    while True:
        words = []
        ports = range(1024)
        for port in ports:
            words.append(