#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or converts a port. """    
    port = int(sys.argv[1])
    if port == 8080:
        port = 80
    else:
        port = int(port)
    
    httpd = HTTPServer(("", port), Handler)
    httpd.serve_forever()

<|/ file ext=.py |>