#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports. """    
    ports = []
    while True:
        ports.append( int( input('Enter a port (1-65535): ') ) )
        if ports[-1] == 255:
            ports.pop()
        else:
            break
    print('\n'.join(map(str, ports)))
    
