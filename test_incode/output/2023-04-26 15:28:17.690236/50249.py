#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words or adds all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1]
        
        if ports == 'all':
            ports = ''
            
        ports = ports.split(',')
        
        for port in ports:
            
            if port == '':
                continue
            
            port = int(port)
            
            if port < 0 or port > 65535:
                sys.exit('Invalid port number: %s' % port)
                
            