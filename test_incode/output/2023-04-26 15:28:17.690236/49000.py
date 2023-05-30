#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers. """    
    
    # Create a simple web server
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start it
    server.serve_forever()

<|/ file filename=