#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    
    # Create a server and listen for connections
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start the server
    server.serve_forever()
