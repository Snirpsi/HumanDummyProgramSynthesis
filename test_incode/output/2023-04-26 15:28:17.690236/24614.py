#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        print("The port is: " + str(port))
        
    else:
        print("Usage: python port-multiplier.py <port>")
        
