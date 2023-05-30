#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    port = int(sys.argv[1])
    
    numbers = [int(n) for n in sys.argv[2:]]
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    httpd.serve_forever()

<|/ file filename=server.py ext=.py |>