#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port. """    
    
    ports = [i for i in range(65535)]
    
    while True:
        
        ports_str = ','.join(str(p) for p in ports)
        
        print('Port %s is %s' % (ports_str, 