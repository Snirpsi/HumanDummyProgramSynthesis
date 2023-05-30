#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and opens all ports. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        print("Port %d is open" % port)
        
        for 