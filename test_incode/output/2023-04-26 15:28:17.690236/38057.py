#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers and returns all ports. """    
    import sys
    
    ports = []
    for arg in sys.argv[1:]:
        try:
            ports.append(int(arg))
        except ValueError:
            pass
    
    for port in ports:
        if port not in ports:
            print(port)
    
