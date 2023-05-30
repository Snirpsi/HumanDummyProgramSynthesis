#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers. """    
    
    # Start a web server
    httpd = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    
    # Wait forever
    httpd.serve_forever()

<|/ file filename=