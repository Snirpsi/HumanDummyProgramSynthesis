#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of numbers or stores all ports. """    
    ports = []
    
    # Read input from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Split on comma
        ports.append(line.split(','))
    
    # Convert list of ports to list of tuples
    ports = map(tuple, ports)
    
    # Convert list of ports to list of integers
    ports = map(int, ports)
    
    # Print the list of ports
    for port in ports:
        print(','.join(map(str, port)))
        
