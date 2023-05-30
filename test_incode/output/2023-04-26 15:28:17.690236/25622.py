#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    server = HTTPServer(('', 8080), BaseHTTPRequestHandler)
    
    print('Starting webserver on port 8080')
    server.serve_forever()
    
