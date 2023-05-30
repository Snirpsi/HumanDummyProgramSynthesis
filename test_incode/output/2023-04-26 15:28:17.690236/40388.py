#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or opens a list of words. """    
    ports = list( map( int, sys.argv[1:] ) )
    ports.sort()
    
    words = []
    for port in ports:
        words.append( f'http://127.0.0.1:{port}' 