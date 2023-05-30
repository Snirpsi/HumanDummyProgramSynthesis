#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    
    port = 8080
    
    # Start a server
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Run the server
    server.serve_forever()
    
