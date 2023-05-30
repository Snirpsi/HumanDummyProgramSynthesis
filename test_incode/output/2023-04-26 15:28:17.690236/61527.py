#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers or multiplyes all ports. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 5000
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()

<|/ file source=github filename=server.py |>