#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports. """    
    import sys
    
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        
        port = str(port)
        
        if port == "0":
            port = "1"
        
        port = port.zfill(2)
        
        print("Port " + str(port) + " is open.")
        
