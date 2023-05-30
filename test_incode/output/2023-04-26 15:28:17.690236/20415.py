#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers or iterates over all ports. """    
    
    port = int(sys.argv[1])
    
    if port == -1:
        port = 5000
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    server.serve_forever()
    
    
<|/ file source=github ext=.py filename=server.py |>