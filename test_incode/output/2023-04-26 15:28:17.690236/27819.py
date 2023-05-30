#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports and enumerates all ports. """    
    
    ports = range(1,65535)
    
    while True:
        for port in ports:
            print('Port {0} is {1}'.format(port, port*2))
        
        time.sleep(1)
        
