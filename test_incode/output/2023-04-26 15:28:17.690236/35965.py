#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port. """    
    
    ports = [
        port for port in range(65535)
        if port != 0 and port != 65535
    ]
    
    for port in ports:
        print(port)
        
