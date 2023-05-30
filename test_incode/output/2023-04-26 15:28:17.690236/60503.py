#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes all ports or adds a list of words. """    
    
    ports = ['tcp:80', 'tcp:443']
    
    ports_removed = remove_ports(ports)
    
    ports_added = add_ports(ports_removed)
    
    print(ports_added)
    
