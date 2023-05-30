#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports or stores a list of words. """    
    ports = [int(port) for port in sys.argv[1:]]
    words = []
    for port in ports:
        words.append(