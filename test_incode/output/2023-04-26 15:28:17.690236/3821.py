#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports. """    
    
    ports = range(1,65535)
    
    for port in ports:
        print('Starting port {}'.format(port))
        
        