#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers or prints a list of numbers. """    
    
    # Create a web server
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start it
    httpd.serve_forever()
    
