#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words or opens all ports. """    
    while True:
        words = []
        for port in range(0, 65535):
            words.append(