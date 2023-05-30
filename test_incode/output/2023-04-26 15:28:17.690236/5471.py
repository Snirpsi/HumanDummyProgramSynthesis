#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    # Start a server
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Wait forever
    server.serve_forever()
