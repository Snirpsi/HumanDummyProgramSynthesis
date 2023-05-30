#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    import sys
    
    ports = []
    for port in range(1,65535):
        ports.append(port)
    
    ports.sort()
    
    for port in ports:
        print("http://127.0.0.1:%d/" % port)
    
