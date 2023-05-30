#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Remove the port from the system
    subprocess.call(['ip', 'link', 'set', port, 'down'])
    
    # Print the port number back out
    print("Port number set to " + port)
    
