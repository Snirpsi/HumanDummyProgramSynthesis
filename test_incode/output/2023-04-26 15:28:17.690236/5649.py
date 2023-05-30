#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of numbers or removes a port. """    
    
    ports = sys.argv[1:]
    
    if len(ports) == 1:
        ports = [ports[0]]
    
    ports = [int(p) for p in ports]
    
    for port in ports:
        
        if port < 0 or port > 65535:
            print('Port must be between 0 and 65535.')
            sys.exit(1)
        
        