#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or opens a port. """    
    import sys
    port = int(sys.argv[1])
    web = HTTPServer(('', port), SimpleHTTPRequestHandler)
    web.