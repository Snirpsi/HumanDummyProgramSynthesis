#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits and opens numbers. """    
    
    port = 8000
    
    # Create a simple web server
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start it
    server.serve_forever()
