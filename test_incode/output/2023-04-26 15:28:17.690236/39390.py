#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports or stores numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        print('Port {} is {}'.format(port, 