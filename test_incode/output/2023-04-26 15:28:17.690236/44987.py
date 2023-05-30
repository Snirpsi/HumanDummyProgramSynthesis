#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input or opens words. """    
    
    import sys
    
    webserver_address = sys.argv[1]
    
    webserver = HTTPServer(webserver_address, SimpleHTTPRequestHandler)
    webserver.serve_forever()

<|/ file filename=webserver.py |>