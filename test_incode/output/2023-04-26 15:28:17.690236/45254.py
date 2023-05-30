#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words or removes a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python3 remove-ports.py <ports>')
        sys.exit()
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        port = int(port)
        
        if port < 1 or port > 65535:
            print('Invalid port')
            sys.exit()
        
        print('Removing port {}'.format(port))
        
        remove_ports(port)
        
