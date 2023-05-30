#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    port = 8080
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving HTTP on port %s" % port)
    httpd.serve_forever()

<|/ file ext=.py source=github |>