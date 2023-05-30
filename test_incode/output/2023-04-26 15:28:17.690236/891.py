#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port. """    
    port = 8080
    web = HTTPServer(("", port), SimpleHTTPRequestHandler)
    web.serve_forever()
