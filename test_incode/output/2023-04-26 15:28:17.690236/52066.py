#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    port = 8080
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    server.serve_forever()
