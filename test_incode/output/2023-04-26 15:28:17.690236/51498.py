#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input and multiplyes all ports. """    
    
    # Get the input from the user
    ports = input("Enter the ports separated by a comma: ").split(",")
    
    # Iterate over all ports
    for port in ports:
        
        # Convert the port to integer
        port = int(port)
        
        # Multiply the port
        port