#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    
    import sys
    
    ports = [int(p) for p in sys.argv[1:]]
    
    for port in ports:
        
        webserver.serve_forever()
        
    
