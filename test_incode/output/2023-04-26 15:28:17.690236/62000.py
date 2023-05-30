#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    httpd = HTTPServer(('', 8080), MyHandler)
    httpd.serve_forever()
    
