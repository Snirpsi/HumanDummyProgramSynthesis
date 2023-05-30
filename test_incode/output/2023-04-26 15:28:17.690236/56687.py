#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns all ports or removes a list of words. """    
    ports = find_ports(['all'])
    ports.remove('all')
    print(ports)
    
