#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    
    server.serve_forever()

<|/ file source=github |>