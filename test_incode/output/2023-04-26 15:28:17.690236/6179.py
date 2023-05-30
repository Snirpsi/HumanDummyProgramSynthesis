#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or prints a port. """    
    
    ports = []
    
    try:
        ports = range(5000, 5999)
    except KeyboardInterrupt:
        pass
    
    for port in ports:
        print('Port %s is open.' % port)
    
    print('\nPress Ctrl-C to quit.')
    
    