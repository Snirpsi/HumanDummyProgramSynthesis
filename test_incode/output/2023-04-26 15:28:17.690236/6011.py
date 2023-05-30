#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    
    # Start a web server
    httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    
    # Start a thread to handle requests
    httpd.serve_forever()

<|/ file filename=