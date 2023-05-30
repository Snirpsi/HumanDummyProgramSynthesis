#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and calculates words. """    
    ports = range(8000, 8100)
    words = []
    for port in ports:
        words.append(