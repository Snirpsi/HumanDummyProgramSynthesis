#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or removes a list of numbers. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Get the list of numbers from the command line
    numbers = sys.argv[2:]
    
    # Add the port number to the list of numbers
    numbers.append(port)
    
    # Print the list of numbers
    print('\n'.join(numbers))
    
    # Start the webserver
    webserver.run(numbers)
    
