#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words and converts all ports. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    for port in range(port, 65535):
        words.append(str(port))
    
    words.sort()
    
    word