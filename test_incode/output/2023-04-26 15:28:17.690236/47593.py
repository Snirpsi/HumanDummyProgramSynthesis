#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and converts numbers. """    
    import sys
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = make_server('', port, MyHandler)
    print('Serving HTTP on port {} ...'.format(port))
    httpd.serve_forever()

<|/ file filename=server.py |>