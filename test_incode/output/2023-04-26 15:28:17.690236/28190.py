#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input. """    
    
    # Create a web server
    server = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    
    # Start it
    server.serve_forever()
    
