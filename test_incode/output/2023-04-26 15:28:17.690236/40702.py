#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports. """    
    
    ports = list( map( int, open('/dev/tty', 'r').read().split() ) )
    
    for port in ports:
        print('Port {}: {}'.format(port, open('/dev/tty', 'r').read().splitlines()[port]))
        
