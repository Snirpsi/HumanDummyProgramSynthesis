#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port. """    
    port = int(sys.argv[1])
    webserver.serve_forever(port=port)

<|/ file filename=webserver.py source=github ext=.py |>