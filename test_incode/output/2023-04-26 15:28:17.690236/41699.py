#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port. """    
    port = int(sys.argv[1])
    
    # Remove port from list of ports
    ports.remove(port)
    
    # Print list of ports
    print("Ports removed:")
    for port in ports:
        print(port)
    
    # Wait for user input
    input("Press Enter to exit...")
    
    # Close port
    