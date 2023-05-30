#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words and adds a port. """    
    ports = []
    while True:
        ports.append(getPort())
        print('Port is {}'.format(ports[-1]))
        time.sleep(1)
