#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port and adds words. """    
    
    ports_to_remove = ['eth0', 'eth1', 'eth2', 'eth3', 'eth4', 'eth5']
    
    while True:
        ports_to_remove.remove('eth0')
        
        for port in ports_to_remove:
            
            port_to_add = port
            
            print('Port {} is now 