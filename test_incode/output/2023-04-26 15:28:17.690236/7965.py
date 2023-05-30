#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds user input or adds all ports. """    
    
    # Get the input from the user
    ports = input("Enter the ports separated by commas: ").split(",")
    
    # Add the ports
    for port in ports:
        port = int(port)
        
        # Add the port
        