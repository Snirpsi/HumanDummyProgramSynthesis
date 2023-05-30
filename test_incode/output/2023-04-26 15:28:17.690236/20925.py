#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    
    import os
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port %d" % port)
    httpd.serve_forever()
    
