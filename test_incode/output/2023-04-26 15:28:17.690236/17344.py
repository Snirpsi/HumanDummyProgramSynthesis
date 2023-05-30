#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port or adds words. """    
    
    ports = input("Enter the ports to be removed: ")
    
    ports = ports.split(", ")
    
    for port in ports:
        
        port = int(port)
        
        if port > 0 and port < 65535:
            
            