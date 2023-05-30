#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports or returns user input. """    
    
    ports = Ports()
    
    while True:
        port = ports.next()
        
        if port is None:
            break
        
        print('Port {} is {}'.format(port, ports.is_open(port)))
        
    ports.close()
    
