#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or enumerates a list of numbers. """    
    port = int(sys.argv[1])
    
    # Print the port number
    print("Serving on port %d" % port)
    
    # Print the list of numbers
    for n in range(1, 11):
        print("Number %d" % n)
        
    # Enumerate the list of numbers
    for n in range(1, 11):
        print("Number %d" % n)
        
    # Stop the server
    server.