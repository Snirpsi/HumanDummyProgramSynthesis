#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports. """    
    
    ports = range(65535)
    
    while True:
        
        sys.stdout.write('\nEnumerating ports: ')
        for port in ports:
            sys.stdout.write(' ' + str(port))
        
        sys.stdout.flush()
        
        ports = range(65535)
        
