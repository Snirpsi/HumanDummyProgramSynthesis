#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port. """    
    
    port = int(sys.argv[1])
    
    while True:
        print("Port is %s" % port)
        
        time.sleep(1)
        
        port += 1
        
        if port > 65535:
            port = 1
            
