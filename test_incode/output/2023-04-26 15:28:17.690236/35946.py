#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port. """    
    port = int(sys.argv[1])
    
    webserver.serve(port)

<|/ file source=github dstars=1 |>