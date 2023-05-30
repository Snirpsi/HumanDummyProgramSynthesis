#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers or converts user input. """    
    
    # Create a web server
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start it
    httpd.serve_forever()
    
