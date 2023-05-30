#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports and multiplyes a list of words. """    
    ports = ports.split(',')
    words = []
    for port in ports:
        words.append(port