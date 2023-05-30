#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and prints all ports. """    
    while True:
        port = random.randint(1,65535)
        print('Port {} is open'.format(port))
        