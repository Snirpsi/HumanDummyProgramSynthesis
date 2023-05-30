#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port or calculates a list of numbers. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Get the list of numbers from the command line
    numbers = sys.argv[2:]
    
    # Remove a port from the list
    numbers.remove(port)
    
    # Print the list
    print("\n".join(numbers))
    
