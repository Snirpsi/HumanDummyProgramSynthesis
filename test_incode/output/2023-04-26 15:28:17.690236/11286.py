#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers or stores user input. """    
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
