#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    httpd = HTTPServer(('', 0), MyHandler)
    httpd.serve_forever()
    
