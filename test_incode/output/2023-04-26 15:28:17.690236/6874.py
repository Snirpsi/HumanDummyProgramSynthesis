#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input. """    
    
    # Start a web server
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    
    # Wait forever for incoming connections
    server.serve_forever()
    
