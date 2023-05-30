#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns all ports or prints words. """    
    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        if arg.startswith('-'):
            ports.append(arg)
        else:
            ports.append(int(arg))
    
    for port in ports:
        print(port)
    
