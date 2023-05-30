#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port. """    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, app)
    httpd.serve_forever()

<|/ file source=github filename=webserver.py |>