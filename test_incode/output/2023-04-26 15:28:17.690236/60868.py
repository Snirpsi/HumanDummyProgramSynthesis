#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    import sys
    port = sys.argv[1]
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving HTTP on port %d" % port)
    httpd.serve_forever()

<|/ file filename=webserver.py ext=.py |>