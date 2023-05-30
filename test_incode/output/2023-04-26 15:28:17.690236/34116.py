#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port. """    
    port = 8080
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    httpd = HTTPServer(('localhost', port), BaseHTTPRequestHandler)
    
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
