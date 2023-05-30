#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port and prints numbers. """    
    ports = [int(i) for i in sys.argv[1:]]
    for port in ports:
        print('Port {} is {}'.format(port, ports[port]))
