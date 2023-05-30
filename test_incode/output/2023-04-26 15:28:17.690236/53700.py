#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port or removes a port. """    
    port = int(sys.argv[1])
    if port == 0: 
        print("No port specified.")
        exit(1)
    elif port == -1:
        print("No port specified.")
        exit(1)
    elif port < 0 or port > 65535:
        print("Port must be between 0 and 65535.")
        exit(1)
    else:
        print("Port %d is now %s." % (port, str(port)))
        
    
<|/ file source=github |>