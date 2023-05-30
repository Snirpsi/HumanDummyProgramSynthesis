#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        port = int(port)
        
        print("Port {} is open".format(port))
        
