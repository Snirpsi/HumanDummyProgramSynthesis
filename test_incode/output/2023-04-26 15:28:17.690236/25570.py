#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input or opens a port. """    
    
    port = int(sys.argv[1])
    
    webserver = HTTPServer(('', port), SimpleHTTPRequestHandler)
    webserver.serve_forever()

<|/ file filename=server.py |>