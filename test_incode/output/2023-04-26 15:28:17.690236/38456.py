#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits and enumerates fruits. """    
    
    import os
    import socket
    import http.server
    import http.client
    
    HOST = 'localhost'
    PORT = 8080
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    httpd = http.server.HTTPServer(('', PORT), Handler)
    
    print('Serving at http://%s:%s/' % (HOST, PORT))
    
    httpd.serve_forever()
    
