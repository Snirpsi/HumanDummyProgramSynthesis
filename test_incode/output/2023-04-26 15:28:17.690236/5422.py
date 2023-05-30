#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers and prints numbers. """    
    
    server_address = ('localhost', 8000)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port 8000...')
    httpd.serve_forever()
