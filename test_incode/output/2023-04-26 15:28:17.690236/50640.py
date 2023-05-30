#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates all ports. """    
    
    # Read input file
    lines = open('input.txt').readlines()
    
    # Initialize variables
    ports = []
    
    # Iterate over all lines
    for line in lines:
        
        # Split line into port name and value
        name, value = line.split('=')
        
        # Append port to list
        ports.append({'name': name, 'value': value})
    
    # Print ports
    print('\n'.join(['{}={}'.format(p['name'], p['value']) for p in ports]))
    
