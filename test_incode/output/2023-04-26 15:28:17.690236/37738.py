#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input and multiplyes a list of numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    
    # Start it
    server.serve_forever()
    
