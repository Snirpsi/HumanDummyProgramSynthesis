#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or stores a port. """    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 8080
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port %s' % port)
    httpd.serve_forever()

<|/ file source=github filename=server.py |>