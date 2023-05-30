#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and prints a list of numbers. """    
    ports = []
    
    for port in range(1, 65535):
        ports.append(port)
        
    print('\n'.join(map(str, ports)))
    
