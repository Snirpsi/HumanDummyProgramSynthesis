#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or converts a list of numbers. """    
    port = int(sys.argv[1])
    
    if port < 0 or port > 65535:
        print("Port must be between 0 and 65535.")
        sys.exit(1)
    
    ports = [int(port)]
    
    if len(sys.argv) > 2:
        ports = sys.argv[2:]
    
    ports.sort()
    
    for port in ports:
        