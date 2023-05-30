#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds all ports and multiplyes a list of numbers. """    
    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        ports.append(int(arg))
    
    ports = list(set(ports))
    
    ports = list(map(lambda x: x * 2, ports))
    
    print(ports)
    
