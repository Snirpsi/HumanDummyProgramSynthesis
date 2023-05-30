#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words or opens all ports. """    
    import sys
    ports = []
    for arg in sys.argv[1:]:
        if arg.startswith('-'):
            ports.append(arg)
        else:
            ports.append(int(arg))
    
    for port in ports:
        openport(port)
        
