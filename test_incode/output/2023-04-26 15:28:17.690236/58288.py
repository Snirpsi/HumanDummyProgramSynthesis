#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    import sys
    import os
    
    port = int(sys.argv[1])
    
    webserver = WebServer()
    webserver.listen(port)
    
    webserver.serve_forever()

<|/ file source=github ext=.py |>