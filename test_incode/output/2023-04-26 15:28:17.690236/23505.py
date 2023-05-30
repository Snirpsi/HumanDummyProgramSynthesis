#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and removes all ports. """    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, MyHandler)
    httpd.serve_forever()

<|/ file ext=.py filename=server.py |>