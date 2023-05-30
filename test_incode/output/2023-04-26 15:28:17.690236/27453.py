#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers. """    
    port = 8000
    
    # Create a simple web server
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Run the server
    httpd.serve_forever()
    
