#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and multiplyes all ports. """    
    port = 1
    while True:
        port = port * 2
        print('Port %d' % port)
        time.sleep(1)
