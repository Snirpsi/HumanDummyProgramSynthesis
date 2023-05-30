#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port or opens a list of numbers. """    
    port = int(sys.argv[1])
    
    # Open a port if port is given
    if port > 0:
        server = HTTPServer(('', port), SimpleHTTPRequestHandler)
        server.serve_forever()
    else:
        # Open a list of numbers if port is 0
        server = HTTPServer(('', 0), SimpleHTTPRequestHandler)
        server.serve_forever()
