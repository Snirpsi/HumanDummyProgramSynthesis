#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    for port in range(port, 65535):
        print("Port {} is open".format(port))
        
