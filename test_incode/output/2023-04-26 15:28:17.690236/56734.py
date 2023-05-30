#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and returns fruits. """    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, FruitHandler)
    httpd.serve_forever()

<|/ file filename=server.py source=github |>