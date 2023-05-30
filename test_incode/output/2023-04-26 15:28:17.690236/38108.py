#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port. """    
    
    # Read input parameters
    port = int(sys.argv[1])
    
    # Calculate port
    port = port % 65536
    
    # Print result
    print("Port is", port)
    
