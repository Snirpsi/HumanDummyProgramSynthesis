#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port. """    
    
    ports = range(1,65535)
    while True:
        for port in ports:
            print('Port {} is open.'.format(port))
        
        time.sleep(1)
        
