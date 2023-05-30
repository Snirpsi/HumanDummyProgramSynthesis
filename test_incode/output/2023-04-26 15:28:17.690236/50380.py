#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    
    import sys
    
    server_address = ('localhost', 8080)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    sa = httpd.socket.getsockname()
    
    print('Serving HTTP on', sa[0]