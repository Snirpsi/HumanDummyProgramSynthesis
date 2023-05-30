#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers or prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8000
    
    webserver = HTTPServer(('', port), SimpleHTTPRequestHandler)
    webserver.serve_forever()

<|/ file source=github filename=webserver.py |>