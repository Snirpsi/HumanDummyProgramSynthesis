#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    
    from http.server import HTTPServer
    
    server = HTTPServer(('', 0), SimpleHTTPRequestHandler)
    
    server.serve_forever()
