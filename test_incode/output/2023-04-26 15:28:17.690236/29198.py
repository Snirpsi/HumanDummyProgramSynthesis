#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and multiplyes a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    port = sys.argv[1]
    
    httpd = HTTPServer(("", port), MyHandler)
    print("Starting server on port %s" % port)
    httpd.serve_forever()
    
