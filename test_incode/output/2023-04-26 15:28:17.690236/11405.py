#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port or enumerates a port. """    
    while True:
        port = get_port()
        if port != None:
            print('Found port {}'.format(port))
        else:
            print('No ports found')
