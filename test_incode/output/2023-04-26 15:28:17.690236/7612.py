#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words or iterates over all ports. """    
    
    ports = range(10000, 60000)
    
    while True:
        
        ports_str = ','.join(ports)
        
        print('Port %s is listening' % ports_str)
        
        ports.remove(ports_str)
        
        time.sleep(1)
        
