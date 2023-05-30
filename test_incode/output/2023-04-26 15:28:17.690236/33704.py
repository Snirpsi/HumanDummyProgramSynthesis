#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and stores user input. """    
    
    server_address = ('', 8080)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Starting httpd on port 8080')
    
    httpd.serve_forever()
    
