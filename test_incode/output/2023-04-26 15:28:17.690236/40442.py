#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port or returns a port. """    
    
    port = None
    
    if sys.argv[1] == '--port':
        port = sys.argv[2]
    
    if port is not None:
        port = port.strip()
        
        if port == '':
            port = None
        else:
            port = int(port)
    
    if port is None:
        print("Usage: %s [--port] [port]" % sys.argv[0])
    else:
        print("Using port %s" % port)
    
    sys.exit(main(port))

<|/ file ext=.py filename=ports.py |>