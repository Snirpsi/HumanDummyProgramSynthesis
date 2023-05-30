#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port or returns a port. """    
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    print("Starting webserver on port %d" % port)
    httpd = make_server('', port, app)
    httpd.serve_forever()

<|/ file ext=.py filename=webserver.py |>