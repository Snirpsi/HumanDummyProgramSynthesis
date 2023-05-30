#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and converts words. """    
    ports = []
    for port in range(1024):
        ports.append(port)
    
    words = []
    for port in ports:
        words.append(str(port) + "