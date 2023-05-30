#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers or iterates over numbers. """    
    
    server_address = ('localhost', 8000)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
