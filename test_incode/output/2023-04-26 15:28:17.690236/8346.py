#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or removes a port. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        port = int(port)
        
        if port > 0:
            
            print("Port ", port, " is open.")
            
        else:
            
            print("Port ", port, " is closed.")
            
            
