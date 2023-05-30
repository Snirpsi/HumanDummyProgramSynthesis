#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port 8080...')
    httpd.serve_forever()
