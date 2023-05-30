#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports or opens a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
        
        if port == 'all':
            ports = range(1024)
        else:
            ports = [int(port)]
            
        for port in ports:
            print('Port {} ({})'.format(port, 