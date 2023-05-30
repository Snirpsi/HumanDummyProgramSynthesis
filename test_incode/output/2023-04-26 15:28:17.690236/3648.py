#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a port and returns all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
        
        print("Port %s is open." % port)
    else:
        print("Usage: %s port" % sys.argv[0])
        
        
