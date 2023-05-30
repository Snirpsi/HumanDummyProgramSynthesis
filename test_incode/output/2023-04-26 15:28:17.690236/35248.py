#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers or calculates all ports. """    
    
    # Read input from stdin
    lines = sys.stdin.readlines()
    
    # Remove all numbers
    numbers = [int(line) for line in lines if not line.isdigit()]
    
    # Remove all calculations
    calculations = [int(line) for line in lines if not line.isdigit()]
    
    # Remove all ports
    ports = [int(line) for line in lines if not line.isdigit()]
    
    # Print the result
    print(numbers)
    print(calculations)
    print(ports)
    
