#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports or returns a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = range(1,65535)
        
    for port in ports:
        print("Port {} is open".format(port))
        
