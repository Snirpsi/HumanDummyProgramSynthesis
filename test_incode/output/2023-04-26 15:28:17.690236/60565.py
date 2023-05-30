#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and prints words. """    
    ports = range(1,65535)
    words = []
    for port in ports:
        words.append(str(port) + ' - 