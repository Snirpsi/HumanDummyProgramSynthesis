#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports and returns words. """    
    ports = range(8000, 8008)
    words = []
    for port in ports:
        words.append(