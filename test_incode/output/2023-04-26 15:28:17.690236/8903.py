#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates numbers and stores all ports. """    
    
    # Read input from stdin
    ports = sys.stdin.read().split()
    
    # Calculate and store ports
    ports = calculate_ports(ports)
    
    # Print output
    print(ports)
    
