#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports or prints a list of words. """    
    ports = range(1,65535)
    words = []
    for port in ports:
        words.append(str(port))
    print('\n'.join(words))
    
