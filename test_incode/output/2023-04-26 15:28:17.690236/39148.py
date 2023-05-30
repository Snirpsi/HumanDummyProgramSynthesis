#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of numbers or calculates a port. """    
    ports = []
    
    # Read input from stdin and store in ports list
    for line in sys.stdin:
        ports.append(int(line))
    
    # Calculate ports based on input from stdin
    ports = calculate_ports(ports)
    
    # Print ports back to stdout
    ports.sort()
    for port in ports:
        print(port)
        
    # Print the result
    print(ports)

<|/ file filename=ports.py |>