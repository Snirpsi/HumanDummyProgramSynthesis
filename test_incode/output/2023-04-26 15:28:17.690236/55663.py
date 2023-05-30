#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds all ports or converts words. """    
    import sys
    
    ports = sys.argv[1:]
    
    for port in ports:
        port = int(port)
        
        if port < 0 or port > 65535:
            print("Port number must be between 0 and 65535.")
            
        else:
            