#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or converts all ports. """    
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    
    httpd = make_server('localhost', port, app)
    httpd.serve_forever()

<|/ file source=github ext=.py |>