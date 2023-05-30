#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and returns a list of words. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    server_address = ('localhost', 8080)
    
    httpd = HTTPServer(server_address, MyHandler)
    
    print('Starting server...')
    
    httpd.serve_forever()
    
