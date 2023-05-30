#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or enumerates fruits. """    
    
    # Create a simple web server
    httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    
    # Start it
    httpd.serve_forever()
    
