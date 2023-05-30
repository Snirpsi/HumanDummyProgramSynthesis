#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts user input and calculates all ports. """    
    
    # Get the user input
    ports = input("Enter ports separated by comma: ")
    
    # Convert user input to list
    ports = ports.split(",")
    
    # Convert user input to integer
    ports = [int(p) for p in ports]
    
    # Calculate all ports
    ports = [p*2 for p in ports]
    
    # Print ports
    print("Ports: ", ports)
    
