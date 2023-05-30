#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    while True:
        
        sys.stdout.write("Port %d\n" % port)
        
        sys.stdout.flush()
        
        time.sleep(1)
        
        port += 1
        
