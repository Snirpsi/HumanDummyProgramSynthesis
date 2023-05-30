#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    import sys
    
    ports = enumerate_ports(sys.argv[1])
    
    for port in ports:
        print("Serving on port %s" % port)
        
    
