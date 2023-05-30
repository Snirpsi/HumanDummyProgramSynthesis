#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    # Start the webserver
    httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()
