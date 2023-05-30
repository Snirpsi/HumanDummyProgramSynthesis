#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and iterates over words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    for i in range(port):
        words.append(