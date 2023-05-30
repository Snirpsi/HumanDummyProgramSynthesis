#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port. """    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, app)
    print('Serving on port {}'.format(port))
    httpd.serve_forever()

<|/ file filename=server.py source=github |>