#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and adds a list of words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for port in range(port, 65535):
        words.append('port %d' % port)
    
    print('\n'.join(words))
    
