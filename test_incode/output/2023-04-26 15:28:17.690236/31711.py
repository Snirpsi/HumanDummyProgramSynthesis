#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints all ports or adds fruits. """    
    
    # Get the port number
    port = int(sys.argv[1])
    
    # Print all ports
    for port in range(1,port+1):
        print("Port {}: 