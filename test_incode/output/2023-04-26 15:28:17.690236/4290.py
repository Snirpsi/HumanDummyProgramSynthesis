#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or adds numbers. """    
    port = int(sys.argv[1])
    
    # Add numbers to the port if needed
    if port % 2 == 0:
        port += 1
    
    # Return the port number
    return port

<|/ file ext=.py filename=