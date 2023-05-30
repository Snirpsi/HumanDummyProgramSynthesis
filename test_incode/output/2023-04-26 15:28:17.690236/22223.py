#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and enumerates a list of words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    for x in range(port):
        words.append(str(x