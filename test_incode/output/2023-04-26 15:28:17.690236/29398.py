#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port. """    
    port = 8080
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    httpd = HTTPServer(("", port), MyHandler)
    
    print("Serving on port 