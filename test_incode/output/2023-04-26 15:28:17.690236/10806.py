#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports or converts a list of words. """    
    
    import sys
    
    ports = sys.argv[1:]
    
    if len(ports) == 0:
        ports = ['all']
    
    for port in ports:
        
        port = int(port)
        
        if port < 0 or port > 65535:
            print("Port must be between 0 and 65535.")
            continue
        
        if port == 0:
            port = 'all'
        
        print("Port %d is %s." % (port, ports[port]))
        
