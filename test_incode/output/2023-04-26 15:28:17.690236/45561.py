#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and enumerates a port. """    
    
    port = 8080
    
    webserver = HTTPServer(("", port), SimpleHTTPRequestHandler)
    webserver.serve_forever()
    
