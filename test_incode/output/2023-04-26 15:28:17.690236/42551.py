#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    httpd = HTTPServer(("", 80), SimpleHTTPRequestHandler)
    httpd.serve_forever()