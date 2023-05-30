#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and adds all ports. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    server.serve_forever()

<|/ file filename=server.py ext=.py |>