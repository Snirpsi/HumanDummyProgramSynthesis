#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a port or removes a port. """    
    
    port = int(sys.argv[1])
    
    if port == -1:
        remove_port()
    else:
        store_port(port)
        
    
<|/ file source=github filename=ports.py |>