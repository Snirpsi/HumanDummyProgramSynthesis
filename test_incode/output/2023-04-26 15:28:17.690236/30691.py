#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port or adds user input. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Get the user input from the command line
    port = int(sys.argv[2])
    
    # Multiply the port number by the user input
    port = port * int(sys.argv[3])
    
    # Add the port number to the user input
    port = int(port) + int(sys.argv[3])
    
    # Print the result
    print(port)
    
