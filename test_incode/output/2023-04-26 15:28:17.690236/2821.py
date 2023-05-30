#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or converts all ports. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    for _ in range(port):
        words.append(