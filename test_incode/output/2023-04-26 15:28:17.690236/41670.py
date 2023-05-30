#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or calculates numbers. """    
    
    port = 8080
    
    server_address = ('localhost', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()

<|/ file source=github |>