#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port. """    
    
    # Get the port number from the command line arguments
    port = int(sys.argv[1])
    
    # Calculate the port number
    port = port + 10
    
    # Print the port number
    print("The port number is {}".format(port))
    
