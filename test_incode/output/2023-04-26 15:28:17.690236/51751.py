#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        print('Port {0} is {1}'.format(port, ports[port]))
    
    print('\nDone.')
    
