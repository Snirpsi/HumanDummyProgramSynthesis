#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, Handler)
    httpd.serve_forever()

<|/ file ext=.py source=github |>