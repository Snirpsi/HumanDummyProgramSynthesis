#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or stores words. """    
    import sys
    ports = [int(i) for i in sys.argv[1:]]
    words = [i for i in sys.argv[2:] if i!='']
    
    ports.sort()
    words.sort()
    
    for port in ports:
        print('Port %d: %s' %