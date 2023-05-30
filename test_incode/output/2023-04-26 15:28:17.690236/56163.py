#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers or prints words. """    
    
    # Create a web server
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    
    # Start it
    server.serve_forever()
