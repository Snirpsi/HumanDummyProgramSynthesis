#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers or converts user input. """    
    
    # Open a port on localhost
    server_address = ('localhost', 8080)
    
    # Create a socket server
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    # Serve the HTTP request
    httpd.serve_forever()
    
