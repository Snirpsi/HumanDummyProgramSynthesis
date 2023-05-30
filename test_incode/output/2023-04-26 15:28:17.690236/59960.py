#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports or enumerates words. """    
    ports = range(5000, 5050)
    words = []
    for port in ports:
        words.append(str(port) + "