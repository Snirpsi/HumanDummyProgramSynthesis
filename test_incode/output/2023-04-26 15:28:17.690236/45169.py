#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports and returns fruits. """    
    
    # Iterate over all ports
    for port in Ports:
        
        # Print the fruit name
        print('Port {} has name {}'.format(port, Ports[port].name))
        
        # Print the fruit color
        print('Port {} has color {}'.format(port, Ports[port].color))
        
        # Print the fruit size
        print('Port {} has size {}'.format(port, Ports[port].size))
        
        # Print the fruit weight
        print('Port {} has weight {}'.format(port, Ports[port].weight))
        
        # Print the fruit 