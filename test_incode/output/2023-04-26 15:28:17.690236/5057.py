#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port. """    
    port = 0
    while True:
        port = port + 1
        print('port is {}'.format(port))
        time.sleep(1)
        
