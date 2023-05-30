#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    web = WebServer(port)
    web.serve_forever()

<|/ file source=github dstars=0 |>