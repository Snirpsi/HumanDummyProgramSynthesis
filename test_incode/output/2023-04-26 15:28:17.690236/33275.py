#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or stores all ports. """    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 8080
    
    httpd = make_server('', port, print_port)
    httpd.serve_forever()

<|/ file filename=server.py ext=.py |>