#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    
    server_address = ('', 8000)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('serving at http://%s:8000' % server_address[0])
    
    httpd.serve_forever()
    
