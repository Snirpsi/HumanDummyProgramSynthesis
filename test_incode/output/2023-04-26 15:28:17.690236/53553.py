#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input and prints all ports. """    
    
    port = 8080
    
    # Create a server
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start server
    server.serve_forever()
    
