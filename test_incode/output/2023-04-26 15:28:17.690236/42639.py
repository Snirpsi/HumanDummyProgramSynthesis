#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers or multiplyes all ports. """    
    
    ports = range(1,65535)
    
    while True:
        for port in ports:
            print('Port {} is {}'.format(port,port*2))
        
        time.sleep(1)
        
