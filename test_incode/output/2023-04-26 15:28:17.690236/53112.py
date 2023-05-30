#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    httpd = HTTPServer(("", 8000), MyHandler)
    httpd.serve_forever()
