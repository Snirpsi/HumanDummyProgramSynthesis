#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and adds fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    fruits = []
    
    for port in range(port, 65535):
        fruits.append(port)
        
    print('\n'.join(map(str, fruits)))
    
