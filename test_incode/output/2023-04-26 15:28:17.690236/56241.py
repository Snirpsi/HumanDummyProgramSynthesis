#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or returns all ports. """    
    ports = []
    
    # Handle the command line arguments
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 1
        
    # Handle the port number
    if port > 65535:
        print('Port number too large')
        exit(1)
    elif port < 1:
        print('Port number too small')
        exit(1)
    
    # Store the port number
    ports.append(port)
    
    # Print the ports
    print('Ports:')
    for port in ports:
        print('\t' + str(port))
    
    # Return the ports
    return ports
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    