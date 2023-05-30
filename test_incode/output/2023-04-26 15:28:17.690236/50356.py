#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates user input or returns all ports. """    
    
    ports = []
    
    # Get the ports list from the user
    ports = input("Enter the ports separated by comma: ").split(",")
    
    # Print the ports list to the screen
    print("Ports: ", ports)
    
    # Return the ports list
    return ports

<|/ file source=github ext=.py |>