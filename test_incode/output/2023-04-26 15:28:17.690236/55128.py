#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input and removes user input. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving on port 8080')
    httpd.serve_forever()
    
